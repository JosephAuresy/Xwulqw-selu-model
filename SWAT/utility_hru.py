# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:45:11 2023

@author: Ayden
"""

import os


def overwrite_hru_param(hru_name, dir2read, param_pos, value):
    hru_path = os.path.join(dir2read, f'{hru_name}.hru')
    
    with open(hru_path) as f:
         lines = f.read().splitlines()
    f.close()  

    item_line = lines[param_pos].split()
    old_item = item_line[0]
    new_item = str("%.3f" % value)
    new_line = lines[param_pos].replace(old_item, new_item)
    lines[param_pos] = new_line  

    f_w = open(hru_path, "w")
    f_w.close()        
    
    for line in lines:
        f_a = open(hru_path, "a")
        line2write = line + '\n'
        f_a.writelines(line2write)
        
        
def get_hru_list (dir2read, id_sub):
    sub_path = f'{dir2read}/{id_sub*10000:09}.sub'
    with open(sub_path) as f:
         lines = f.read().splitlines()
    f.close()
    
    for line in lines:
        if 'HRU: General' in line:
            id_line = lines.index(line)
            break
    line_sub = lines[id_line+1:]
    hru_list = []
    for line in line_sub:
        hru_num =line.split('.')[0]
        hru_list.append(hru_num)
    return hru_list