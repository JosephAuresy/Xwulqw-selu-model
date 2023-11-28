# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 14:46:11 2023

@author: Ayden
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
input_file = 'C:/Users/Ayden/Documents/QGIS/muse/6_6_v5_koki/koki.gpt'
out_file = 'C:/Users/Ayden/Documents/QGIS/muse/6_6_v5_koki/test.gpt'

df_well_schedule = pd.read_csv('C:/Users/Ayden/Documents/QGIS/aquifer/gwells/Pumping_schedule.csv')

wells = df_well_schedule.well_id.unique()

i=0
df_well_i = df_well_schedule[df_well_schedule.well_id==wells[i]]


f_r = open(input_file, 'r')
mf_lines = f_r.readlines()
f_r.close()
f_w = open(out_file, 'w')
f_w.close()

id_line= 489965
top = mf_lines[:id_line]
f_a = open(out_file, 'a')
f_a.writelines(top)
f_a.close()

for k in range(len(mf_lines)):
    if  "well__" in mf_lines[k]:
        id_line = mf_lines[k]
        wellNum = mf_lines[k][27:len(mf_lines[k])-2]
        df_well_i =  df_well_schedule[df_well_schedule.well_id==wellNum]
        df_well_i = df_well_i.reset_index()
        print(id_line)
        for l in range (k, k+19):
            f_a = open(out_file, 'a')
            f_a.writelines(mf_lines[l])
            f_a.close()
        f_a = open(out_file, 'a')
        f_a.close()
        for i in range(df_well_i.shape[0]):
            f_a = open(out_file, 'a')
            start_date = df_well_i['t0 (days)'][i]
            end_date = df_well_i['tn (days)'][i]
            rate_1 = df_well_i['rate (m3/d)'][i]
            f_a.writelines('        item\n')
            f_a.writelines(f'          StartTime = {start_date}\n')
            f_a.writelines(f'          EndTime = {end_date}\n')
            f_a.writelines(f'          PumpingRate = {rate_1}\n')
            f_a.writelines('          GwtConcentrations = <>\n')
            if i == df_well_i.shape[0]-1:
                f_a.writelines('        end> \n')
            else:
                f_a.writelines('        end\n')
            f_a.close()
        for l in range (k+24, k+114):
            f_a = open(out_file, 'a')
            f_a.writelines(mf_lines[l])
            f_a.close()
        f_a = open(out_file, 'a')
        f_a.close()

id_line= 645803
top = mf_lines[id_line:]
f_a = open(out_file, 'a')
f_a.writelines(top)
f_a.close()

# f_a = open(out_file, 'a')
# k = k + 19
# f_a.writelines(mf_lines[k])
# f_a.close()
            

        # for i in range(0, id_line+18):
        #     # if  wells[0/ in line:
        #         # break
        #     # else:
        #     f_a = open(out_file, 'a')
        #     f_a.writelines(mf_lines[i])
        #     f_a.close()  
           


    # else:
    #     continue
# print(id_line)
# print(mf_lines[id_line])    
        
# line_set_above = mf_lines[:id_line]      
# line_set_below = mf_lines[id_line:]      


# for i in range(0, id_line+18):
#     # if  wells[0/ in line:
#         # break
#     # else:
#     f_a = open(out_file, 'a')
#     f_a.writelines(mf_lines[i])
#     f_a.close()  

