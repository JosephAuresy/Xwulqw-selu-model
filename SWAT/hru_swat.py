# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:47:09 2023

@author: Ayden
"""

# import fortranformat as ff
import os
import subprocess
from utility_swmf import get_hru_list
from utility_swmf import overwrite_hru_param
# import rpy2
# from rpy2 import robjects

# Identify changes in forestry
# Read polygons by years (3)
# Logged subbasin location
# Closest HRU to the logged area

#Read HRUs by subbasin
hru_list_1 = get_hru_list (dir2read='txtInOut', id_sub=1)
hru_list_2 = get_hru_list (dir2read='txtInOut', id_sub=2)

# Modify HRU files parameters
# 1 HRU file, one parameter change, in line 4
overwrite_hru_param(hru_name='000010001', dir2read='txtInOut', param_pos=4, value=0.12)
overwrite_hru_param(hru_name='000010001', dir2read='txtInOut', param_pos=9, value=0.25)
overwrite_hru_param(hru_name='000010003', dir2read='txtInOut', param_pos=9, value=0.30)

# # Run swat
os.chdir('C:/Users/Ayden/Documents/QGIS/m08_23/k8_23/mua/Scenarios/Default/TxtInOut2')
subprocess.call('"C:/Users/Ayden/Documents/QGIS/m08_23/k8_23/mua/Scenarios/Default/TxtInOut2/Rev685_64rel.exe"')

# # Variation of parameters with R-swat? (Using R from python)
# os.environ['R_HOME'] = 'C:/PROGRA~1/R/R-43~1.0'
# from rpy2.robjects.packages import importr

# shiny= importr("shiny")
# runApp("C:\\R-SWAT-master\\R-SWAT-master")


# The result of the function is returned to the Python Environment