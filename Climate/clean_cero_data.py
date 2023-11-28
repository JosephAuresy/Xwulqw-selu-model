# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:31:05 2023

@author: Ayden
"""

import pandas as pd

df = pd.read_csv('C:/Users/Ayden/Documents/QGIS/precip/swat/LC_all_comb.csv')

df['Precip'].fillna(df['Pre2'], inplace=True)

df.to_csv('LC_all_2.csv', index=False)