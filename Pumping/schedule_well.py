# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:54:29 2023

@author: Ayden
"""


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
file_well= 'C:/Users/Ayden/Documents/QGIS/aquifer/gwells/well.csv'

df_well = pd.read_csv(file_well)

sub_attributes= ['well_tag_number','finished_well_depth_ft-bgl', 
                 'bedrock_depth_ft-bgl','static_water_level_ft-btoc',
                 'well_yield_usgpm','well_yield_unit_code','aquifer_id',
                 'latitude_Decdeg','longitude_Decdeg','utm_northing',
                 'utm_easting', 'construction_end_date']

df_well_new=df_well[sub_attributes]

df_well_new.dropna(subset = ['aquifer_id'], inplace=True)

df_well_new.aquifer_id=df_well_new.aquifer_id.astype(int)

well_list=df_well_new.aquifer_id.unique()
new_well_list=[198,201,202,185,186,188,197,199]
df_well_new_1=df_well_new.copy()
df_well_new_1.index=df_well_new_1.aquifer_id
df_well_new_select=df_well_new_1.loc[new_well_list,:]
#df_well_new_select[df_well_new_select.aquifer_id==186]
new_column= ['well_number','finished_well_depth', 'bedrock_depth',
             'static_water_level', 'well_yield','well_yield_unit',
             'aquifer_id','latitude','longitude','north','east', 'date']

df_well_new_select.columns = new_column
df_well_new_select.date = pd.to_datetime(df_well_new_select.date)
df_well_new_select.index = np.arange(0, df_well_new_select.shape[0])

#Calculation of yield in m3/s - convert units
yiled_units = df_well_new_select.well_yield_unit.unique()
df_well_new_select[df_well_new_select.well_yield_unit=='DRY']=np.nan
df_well_new_select.insert(df_well_new_select.shape[1], "rate_cumec", np.nan)
for i in range(df_well_new_select.shape[0]):
    if df_well_new_select.well_yield_unit[i]=='USGPM':
        df_well_new_select.rate_cumec[i] =  df_well_new_select.well_yield[i]/(60*264.173)
    else:
        df_well_new_select.rate_cumec[i] =  df_well_new_select.well_yield[i]/(60*219.968)

df_well_new_Final = df_well_new_select.copy()        
df_well_new_Final.rate_cumec[df_well_new_Final.rate_cumec==0]=np.nan
df_well_new_Final = df_well_new_Final.dropna(subset=['date', 'rate_cumec'])  
# Covert depth units from ft to m      
df_well_new_Final.finished_well_depth = df_well_new_Final.finished_well_depth/3.28
df_well_new_Final.bedrock_depth = df_well_new_Final.bedrock_depth/3.28
df_well_new_Final.static_water_level = df_well_new_Final.static_water_level/3.28
new_column= ['well_number','latitude','longitude','north','east',
             'date', 'finished_well_depth', 'bedrock_depth', 'static_water_level',
             'rate_cumec']
df_well_new_Final = df_well_new_Final[new_column]
df_well_new_Final.columns = ['well_number','latitude','longitude','Y','X',
             'date', 'well_depth', 'bedrock', 'water_level', 'rate']

df_well_new_Final.insert(1,'well_id', np.nan)

for i in range(df_well_new_Final.shape[0]):
    df_well_new_Final.well_id[i]=f'well__{i+1}'
    


#Time to start pumping and to stop -create two columns according to the construction time and 5 months pumping every year
df_well_Final = df_well_new_Final.copy()
df_well_Final.to_csv('well_loc.csv')

df_well_Final.insert(df_well_Final.shape[1], 't_initial', np.nan)
df_well_Final.insert(df_well_Final.shape[1], 't_final', np.nan)

df = df_well_Final.copy()
df.index = np.arange(0, df.shape[0])
start_yr = 2000
end_yr = 2021
num_yrs = end_yr - start_yr

def schedule_pump (df, i, start_yr, end_yr):
    year0 = df.date[i].year
    pump_i, pump_f =[], []
    if year0 < start_yr:
        for year in range(start_yr, end_yr):
            on_time = pd.to_datetime(f'{year}-05-01')
            off_time = pd.to_datetime(f'{year}-09-30')
            pump_i.append(on_time)
            pump_f.append(off_time)
        # day_initial = pd.Series(pump_i)
    else:
        month0 = df.date[i].month
        if month0 > 5:
            year0 = year0 + 1
        for year in range(year0, end_yr):
            on_time = pd.to_datetime(f'{year}-05-01')
            off_time = pd.to_datetime(f'{year}-09-30')
            pump_i.append(on_time)
            pump_f.append(off_time)
        # day_initial = pd.Series(pump_i)
    df_schedule = pd.DataFrame({'Start_date': pump_i, 'End_date': pump_f})
    start_date = pd.to_datetime(f'{start_yr}-01-01')
    diff_st, diff_end = [], []
    diff_day_st, diff_day_end = [], []
    for j in range(df_schedule.shape[0]):
        diff_0 = (df_schedule.Start_date[j] - start_date).total_seconds()
        diff_n = (df_schedule.End_date[j] - start_date).total_seconds()
        diff_st.append(diff_0)
        diff_end.append(diff_n)
        diff_d0 = (df_schedule.Start_date[j] - start_date).days
        diff_dn = (df_schedule.End_date[j] - start_date).days
        diff_day_st.append(diff_d0)
        diff_day_end.append(diff_dn)
        
    df_schedule.insert(df_schedule.shape[1], 't0', diff_st)
    df_schedule.insert(df_schedule.shape[1], 'tn', diff_end)
    df_schedule.insert(df_schedule.shape[1], 't0 (days)', diff_day_st)
    df_schedule.insert(df_schedule.shape[1], 'tn (days)', diff_day_end)    
    df_schedule.insert(df_schedule.shape[1], 'rate', df.rate[i]*-1)    
    df_schedule.insert(df_schedule.shape[1], 'rate (m3/d)', df.rate[i]*-86400)    
    df_schedule.insert(df_schedule.shape[1], 'well_number', df.well_number[i]) 
    df_schedule.insert(df_schedule.shape[1], 'well_id', f'well__{i+1}')     
    
    return df_schedule
        # day_initial = pd.Series(pump_i)
    # sec_initial = day_initial.apply(timedelta.total_seconds)
    # sec_final = sec_initial + (31+30+31+31)*24*3600

df_pumping = pd.DataFrame()
for i in range (df.shape[0]):
    df_well = schedule_pump(df, i, start_yr, end_yr)
    df_pumping = pd.concat([df_pumping, df_well], axis=0)
    print (f'Completed for {df.well_number[i]}')
df_pumping.to_csv('Pumping_schedule.csv')








