# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:15:49 2023

@author: Ayden
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import geopandas as gpd
from matplotlib.tri import Triangulation, LinearTriInterpolator
import rasterio
from shapely.geometry import Point
from rasterio.crs import CRS

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

vec_bed_rock = df_well_new_select['bedrock_depth_ft-bgl'].values
for i in range (len(vec_bed_rock)):
    if np.isnan(vec_bed_rock[i]):
        vec_bed_rock[i]=-9999 

df_well_new_select['bedrock_depth_ft-bgl']=vec_bed_rock
new_column= ['well_number','finished_well_depth', 'bedrock_depth',
             'static_water_level', 'well_yield','well_yield_unit',
             'aquifer_id','latitude','longitude','north','east', 'date']
df_well_new_select.columns=new_column
df_well_above=df_well_new_select[df_well_new_select.finished_well_depth>df_well_new_select.bedrock_depth]
vec_bed_rock[vec_bed_rock==-9999]=np.nan
df_well_new_select.bedrock_depth=vec_bed_rock
df_well_new_select1=df_well_new_select.dropna()

# w198 = df_well_new_select1[df_well_new_select1.aquifer_id==202]
# vec_lat = w198['latitude'].values
# vec_lon = w198['longitude'].values
# vec_bd = w198['bedrock_depth'].values
# xs = vec_lon
# ys = vec_lat
# zs = vec_bd
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(xs,ys,zs)
# plt.show()

vec_lat = df_well_new_select1['latitude'].values
vec_lon = df_well_new_select1['longitude'].values
vec_bd = df_well_new_select1['bedrock_depth'].values
xs = vec_lon
ys = vec_lat
zs = vec_bd
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs,ys,zs)
plt.show()

df3d = df_well_new_select1[['north','east','bedrock_depth']]
df3d.columns = ['lat','lon','depth']

# combine lat and lon column to a shapely Point() object
df3d['geometry'] = df3d.apply(lambda x: Point((float(x.lon), float(x.lat))), axis=1)
df3d = gpd.GeoDataFrame(df3d, geometry='geometry')

# proj WGS84
df3d.crs= "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"
df3d.to_file('MyGeometries.shp', driver='ESRI Shapefile')

points3d = gpd.read_file('MyGeometries.shp')
print(points3d.head())
print(points3d.crs)

#Get numpy array with XYZ point data
totalPointsArray = np.zeros([points3d.shape[0],3])
#iteration over the geopandas dataframe
for index, point in points3d.iterrows():
    pointArray = np.array([point.geometry.coords.xy[0][0],point.geometry.coords.xy[1][0],point['depth']])
    totalPointsArray[index] = pointArray
totalPointsArray[:5,:]

#Required elements for the triangular interpolation
#triangulation function
triFn = Triangulation(totalPointsArray[:,0],totalPointsArray[:,1])
#linear triangule interpolator funtion
linTriFn = LinearTriInterpolator(triFn,totalPointsArray[:,2])

#define raster resolution in (m)
rasterRes = 100
xCoords = np.arange(totalPointsArray[:,0].min(), totalPointsArray[:,0].max()+rasterRes, rasterRes)
yCoords = np.arange(totalPointsArray[:,1].min(), totalPointsArray[:,1].max()+rasterRes, rasterRes)
zCoords = np.zeros([yCoords.shape[0],xCoords.shape[0]])

#loop among each cell in the raster extension
for indexX, x in np.ndenumerate(xCoords):
    for indexY, y in np.ndenumerate(yCoords):
        tempZ = linTriFn(x,y)
        #filtering masked values
        if tempZ == tempZ:
            zCoords[indexY,indexX]=tempZ
        else:
            zCoords[indexY,indexX]=np.nan
            
#preliminary representation of the interpolated values
plt.imshow(zCoords)






