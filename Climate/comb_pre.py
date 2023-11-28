# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:02:16 2023

@author: Ayden
"""

import pandas as pd
import numpy as np
#import os

#Combining data - all years in one excel
# directory = 'C:/Users/Ayden/OneDrive - University of Victoria/Climate/stations/SL_1017230_p'
directory = 'C:/Users/Ayden/Documents/QGIS/precip/swat/'
# csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

# combined_data = pd.DataFrame()

# for file in csv_files:
#     file_path = os.path.join(directory, file)
#     data = pd.read_csv(file_path)
#     combined_data = pd.concat([combined_data, data], ignore_index=True)

# combined_vector = combined_data.values

# combined_data.to_csv('SL_all_comb.csv', index=False)

#------------------------------------------------------------

# # Read the CSV file
#input_file = 'LC_all_comb.csv'
#df = pd.read_csv(input_file)
df = pd.read_csv('LC_all_comb.csv')


# # fill missing values with -99
# v_Tmax = df['Tmax'].values
# for i in range (len(v_Tmax)):
#     if np.isnan(v_Tmax[i]):
#         v_Tmax[i]=-99

# v_Tmin = df['Tmin'].values
# for i in range (len(v_Tmin)):
#     if np.isnan(v_Tmin[i]):
#         v_Tmin[i]=-99

# df2d = df[['Tmax','Tmin']]

df1 = df['Precip'].values
df2 = df['Pre2'].values
for i in range (len(df)):
    if np.isnan(df[i]):
        #df[i]=-99
        df['Precip'].fillna(df['Pre2'], inplace=True)
        
# Create a new DataFrame with the extracted column (optional)
#df2d = pd.DataFrame({'19930101': df})
# new_data = pd.DataFrame({'19930101': df2d})

# Save the extracted column to a new CSV file
output_file = 'SL_all_comb_2.csv'
#df2d.to_csv(output_file, index=False)


