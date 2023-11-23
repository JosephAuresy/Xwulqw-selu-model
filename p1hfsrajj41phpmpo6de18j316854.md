**XC MODELING NOTES with SWAT-MODFLOW**

*Describe challenges and results as you work. This is about documenting
for scientific reproducibility. Someone should be able to use these
notes to reproduce what you have done.*

The updated version of the model has input data from:

**SWAT**: DEM, Soil, Land use, Surface water use,

**MODFLOW**: Aquifer polygons, K, Ss, Sy

**Soil** information: Paper

There is a big quantity of soils in the map which is causing mulitple
HRUs to desapear in the lower area of the watershed. The reason behind
this is that the resolution of the soils there is more detailed.

How was the process to input soil data?

What are the soils that don't have information?

**Land use:**

What are the simplifications of land use?

How many types of land use are we using and why?

**Water use:**

What are the reports and data available that we have been using?

**Options evaluated:**

Aquifer recharge, Dugouts, base case

What are the differences?

What can we conclude from this assessment?

**Model responses to changes**

Parameters

**Analysis of forestry**

Parameters

Runs

**Drivers analysis**

Climate, Land use, water use

Why do some researchers argue that land use and water use are one
driver?

**Optimization**

Sharing process

**Data visualization**

Ideas

**Model version documentation**

+-------+-----------------+-------------------+-----------------------+
| Date/ | File/folder     | Change made from  | Result -- does it     |
| Ve    | name/location   | previous version  | make sense?           |
| rsion |                 |                   |                       |
+=======+=================+===================+=======================+
| 8/1   | XC8_1           | wells activated   | -                     |
| /2023 |                 | 460               |                       |
|       |                 |                   |                       |
|       |                 | daily simulation  |                       |
|       |                 |                   |                       |
|       |                 | new geology, K,   |                       |
|       |                 | Ss, Sy, aquifer   |                       |
|       |                 | separation by     |                       |
|       |                 | polygons          |                       |
+-------+-----------------+-------------------+-----------------------+
| 6/9   | XC6_9           | wells activated   | -                     |
| /2023 |                 | 460               |                       |
|       |                 |                   |                       |
|       |                 | daily simulation  |                       |
+-------+-----------------+-------------------+-----------------------+
| 6/8   | XC6_8           | wells activated   | -                     |
| /2023 |                 | 460               |                       |
|       |                 |                   |                       |
|       |                 | minus the wells   |                       |
|       |                 | in the aquifer    |                       |
|       |                 | 197 in the river  |                       |
|       |                 | corner            |                       |
+-------+-----------------+-------------------+-----------------------+
| 6/7   | XC6_7_V2        | wells activated   | -                     |
| /2023 |                 | 460               |                       |
+-------+-----------------+-------------------+-----------------------+
| 6/7   | XC6_7           | wells activated   | -                     |
| /2023 |                 | 460               |                       |
|       |                 |                   |                       |
|       |                 | Aquifer recharge  |                       |
|       |                 |                   |                       |
|       |                 | 4 points 50 m3/s  |                       |
+-------+-----------------+-------------------+-----------------------+
| 6/6   | XC6_6_V2        | wells activated   | -                     |
| /2023 |                 | 460               |                       |
|       |                 |                   |                       |
|       |                 | Wetland 2         |                       |
|       |                 |                   |                       |
|       |                 | groundwater       |                       |
|       |                 | volume m3         |                       |
+-------+-----------------+-------------------+-----------------------+
| 6/6   | XC6_6           | no wells          | -                     |
| /2023 |                 | activated         |                       |
|       |                 |                   |                       |
|       |                 | Wetland subbasins |                       |
|       |                 | 3, 4              |                       |
|       |                 |                   |                       |
|       |                 | groundwater       |                       |
|       |                 | volume m3         |                       |
|       |                 | required in 5     |                       |
|       |                 | months is the     |                       |
|       |                 | capacity of the   |                       |
|       |                 | wetlands (check   |                       |
|       |                 | if is water       |                       |
|       |                 | licenses or a     |                       |
|       |                 | calculation)      |                       |
+-------+-----------------+-------------------+-----------------------+
| 5/26  | XC_5_26         | no wells          | -                     |
| /2023 |                 | activated         |                       |
|       |                 |                   |                       |
|       |                 | no wetlands       |                       |
|       |                 |                   |                       |
|       |                 | mimic aquifers    |                       |
|       |                 | recharge all the  |                       |
|       |                 | way               |                       |
|       |                 |                   |                       |
|       |                 | extraction of     |                       |
|       |                 | water is the same |                       |
|       |                 | as injection      |                       |
+-------+-----------------+-------------------+-----------------------+
| 5/31  | XC2.0           | -   Wells are     | -   Comparison        |
| /2023 |                 |     added with    |     between observed  |
|       |                 |     pumping       |     and simulated WTD |
|       |                 |                   |     and streamflow    |
|       |                 | -   Observation   |                       |
|       |                 |     from          |                       |
|       |                 |     streamflow    |                       |
|       |                 |     and WTD is    |                       |
|       |                 |     added         |                       |
+-------+-----------------+-------------------+-----------------------+
| 5/26  | XC2.0           | -   3 layers      | -   There is an       |
| /2023 |                 |     running for   |     accumulation of   |
|       |                 |     the first     |     groundwater       |
|       |                 |     time          |     volume, because   |
|       |                 |                   |     there are no      |
|       |                 | -   30 minutes to |     boundaries taking |
|       |                 |     run           |     water out, but    |
|       |                 |                   |     also because I am |
|       |                 |                   |     working in the    |
|       |                 |                   |     wells pumping.    |
|       |                 |                   |                       |
|       |                 |                   | -   The values of GW  |
|       |                 |                   |     discharge are     |
|       |                 |                   |     more credible, we |
|       |                 |                   |     still don't have  |
|       |                 |                   |     positive values,  |
|       |                 |                   |     which means the   |
|       |                 |                   |     water is not      |
|       |                 |                   |     entering the      |
|       |                 |                   |     aquifer from the  |
|       |                 |                   |     river.            |
+-------+-----------------+-------------------+-----------------------+
| 04/12 | C:\\Users\      | -   SWAT-MODFLOW  |                       |
| /2023 | \auresy\\Docume |     model         |                       |
|       | nts\\QGIS\\Kos\ |                   |                       |
|       | \m02_23\\sm4_12 | -   Changes in    |                       |
|       |                 |     the number of |                       |
|       |                 |     groundwater   |                       |
|       |                 |     layers (3)    |                       |
+-------+-----------------+-------------------+-----------------------+
| 03/09 | C:\\Users       | -   SWAT-MODFLOW  | The model is running  |
| /2023 | \\auresy\\Docum |     model         | with one groundwater  |
|       | ents\\QGIS\\Kos |                   | layer connected       |
|       | \\m02_23\\sm3_9 | -   Groundwater   |                       |
|       |                 |     with flopy    |                       |
|       |                 |     inside QGIS   |                       |
|       |                 |     (1 layer)     |                       |
+-------+-----------------+-------------------+-----------------------+
| 02/23 | C:\\Use         | -   SWAT model    |                       |
| /2023 | rs\\auresy\\Doc |                   |                       |
|       | uments\\QGIS\\K | -   This SWAT     |                       |
|       | os\\m02_23\\k21 |     model is not  |                       |
|       |                 |     in the        |                       |
|       |                 |     version PLUS  |                       |
|       |                 |                   |                       |
|       |                 | -   CFSR Global   |                       |
|       |                 |     Weather Data  |                       |
|       |                 |     for SWAT      |                       |
|       |                 |     1979-2014     |                       |
|       |                 |                   |                       |
|       |                 | ```{=html}        |                       |
|       |                 | <!-- -->          |                       |
|       |                 | ```               |                       |
|       |                 | -   Land use 2000 |                       |
+-------+-----------------+-------------------+-----------------------+
| 25/   |                 | -   Resolution    | -   The results are   |
| 07/22 |                 |     improved from |     coherent with the |
|       |                 |     90 m to 30 m  |     input data.       |
|       |                 |                   |                       |
|       |                 | -   Includes an   |                       |
|       |                 |     area outside  |                       |
|       |                 |     of the        |                       |
|       |                 |     watershed     |                       |
|       |                 |     boundary to   |                       |
|       |                 |     have better   |                       |
|       |                 |     water         |                       |
|       |                 |     movement      |                       |
+-------+-----------------+-------------------+-----------------------+
| 14/   | x_swat_0.1      | -   First model   | -   The river is not  |
| 07/22 |                 |                   |     connected         |
|       |                 |                   |                       |
|       |                 |                   | -   The boundary is   |
|       |                 |                   |     too narrow to the |
|       |                 |                   |     watershed         |
+-------+-----------------+-------------------+-----------------------+

To do:

-   ~~Improve resolution of the watershed to get the river connected.~~

```{=html}
<!-- -->
```
-   ~~Cover a wider area to ensure all sub catchments~~

-   Define the point to close the watershed with coordinates.

-   Modify the land use and the soil

Date: 7/15/2022

The next document explains the process to prepare the Koksilah model in
SWAT

1.  DEM: Digital Elevation Model

2.  Land use

3.  Soil

**Steps to create a DEM**

**1. Obtaining SRTM DEM data**

**90x90 m** : <https://srtm.csi.cgiar.org/>

**Product**: SRTM 90m DEM Version 4 **Data File Name**: srtm_12_03.zip
**Mask File Name**: srtm_mk_12_03.zip **Latitude Min**: 125 S **Max**:
120 S **Longitude Min**: 45 E **Max**: 50 E **Center Point Lat**: 122.5
S **Long**: 47.5 E

![](./image1.png){width="1.9270833333333333in"
height="1.9270833333333333in"}![](./image2.png){width="1.96875in"
height="1.96875in"}

**30x30 m** : <http://earthexplorer.usgs.gov/>

**2. Clipping the grids**

Raster → Extraction → Clipper

**3. Merging the grids**

There is no need to merge other files because the area is small.

**4. Reprojecting the grid**

Projection: EPSG: 32610 WSG 84 / UTM zone 10N

Units: meters

No data value: -32768

**5. Masking a DEM**

DEM to be delineated, is done for two reasons:

1\. To reduce the amount of time that delineation takes.

2\. To improve the accuracy of delineation. Latitude

Use a shapefile for the Koksilah area bigger than the watershed

**Calibration**

1.  **Problem:**

-   Predicting evapotranspiration change crop parameters

```{=html}
<!-- -->
```
-   Having wrong flow, change parameters such as curve number, manning
    coefficient.

RSwat run

Obs output form

SWAT [tree
growth](https://engineering.purdue.edu/mapserve/LTHIA7/modified_swat_for_tree_growth_simulation.html)
simulation (Leaf Area Index) LAI

Qi, J., Kang, X., Li, S., & Meng, F. (2022). Evaluating Impacts of
Detailed Land Use and Management Inputs on the Accuracy and Resolution
of SWAT Predictions in an Experimental Watershed. *Water*, *14*(15),
2352.

[AAFC Semi-Decadal Land Use Time
Series](https://open.canada.ca/data/en/dataset/fa84a70f-03ad-4946-b0f8-a3b481dd5248)

2000, 2005, 2010, 2015, 2020

Resolution: 30x30 m

Soil types

<https://catalogue.data.gov.bc.ca/dataset/soil-survey-spatial-view>

**GDAL is not install, no projection**

**Things to do:**

-   **Get the land use maps from previous years 1960, 1965, 1970, 1975,
    1980, 1985, 1990, 1995**

```{=html}
<!-- -->
```
-   **Modify the HK considering spatial distribution**

-   **Modify Ss, Sy considering spatial distribution**

-   **5 meters first layer, all same**

**Convergence problems**

When building the swat model, you need to add the areas of the HRUs in
QGIS

Convergence: Modflow options

Modify the max number of iterations, check the convergence tolerance,
acceleration parameter (smaller).

Water budget: Modify recharge, K values (too small or too high)

NTW for drying problems

Initial Water Table Depth, boundary conditions

The problem was solved changing to higher K values considering ranges of
the report of Mike Wei, as well as the Ss, and Sy accordingly. Also,
time was modified to match models exactly.

**6/19/2023**

**Land use options**

[**https://www.youtube.com/watch?v=AhdjLf-Ux0A&t=1s**](https://www.youtube.com/watch?v=AhdjLf-Ux0A&t=1s)

How to modify the land use considering the HRUs

**Soil type**

Soil Survey Spatial View

iMapBC:
<https://www2.gov.bc.ca/gov/content/data/geographic-data-services/web-based-mapping/imapbc>

[Deriving](https://doi.pangaea.de/10.1594/PANGAEA.877298) Canada-wide
soils dataset for use in Soil and Water Assessment Tool (SWAT).
[Paper](https://essd.copernicus.org/articles/10/1673/2018/)

SWAT2012.mdb adding new types of soils in access

**HRUs**

**Climate distribution**

**Spatial groundwater parameters**

**Aquifer thickness**

**K, Ss, Sy**

**What are the files that can be modified?**

**Plan June-July 2023**

+---+---+---------------------------------------------------------------+
| D |   |                                                               |
| a |   |                                                               |
| t |   |                                                               |
| e |   |                                                               |
+===+===+===============================================================+
| 1 | 2 |                                                               |
| 7 | 1 |                                                               |
| - | - |                                                               |
| J | J |                                                               |
| u | u |                                                               |
| l | l |                                                               |
+---+---+---------------------------------------------------------------+
| 1 | 1 | Run PEST and Parallel PEST: Specify a path to the model       |
| 0 | 4 | folder, Initial run for adjusting weights, perform a parallel |
| - | - | processing with the \"BeoPEST\" (**1 day**)                   |
| J | J |                                                               |
| u | u | Organize results information in a presentation (**1 day**)    |
| l | l |                                                               |
|   |   | Writing result section of the paper (**2 days**)              |
+---+---+---------------------------------------------------------------+
| 3 | 7 | Set up and write swatmf.con file, Build template files:       |
| - | - | MODFLOW pval, SWAT model.in file (**1 day**)                  |
| J | J |                                                               |
| u | u | Build instruction files: Streamflow (SWAT), match it with     |
| l | l | stf_obd file (SWAT), Depth to watertable (MODFLOW), match it  |
|   |   | with dtw_obd file (MODFLOW) (**1 day**)                       |
|   |   |                                                               |
|   |   | Analyse results of multiple runs, including and excluding     |
|   |   | parameters variations (**2 day**)                             |
+---+---+---------------------------------------------------------------+
| 2 | 3 | PEST (Parameter ESTimation Tool), What are the                |
| 6 | 0 | \*.template(.tpl) and instruction(.ins) files?,               |
| - | - |                                                               |
| J | J | Setting up PEST, Middle Bosque SWAT-MODFLOW Model, Spatial    |
| u | u | Parameterization (Zonal Approach & Pilot Points) (**1 day**)  |
| n | n |                                                               |
|   |   | Create PEST control file: Assign parameter group name, Adjust |
|   |   | initial parameter values and their ranges, Assign parameter   |
|   |   | group name, Provide actual observed values to control file,   |
|   |   | Create new control file with settings (**1 day**)             |
|   |   |                                                               |
|   |   | Meeting with Sacha to review codes in python (**1 day**)      |
|   |   |                                                               |
|   |   | Working on the codes (**1 day**)                              |
+---+---+---------------------------------------------------------------+
| 1 | 2 | Review                                                        |
| 9 | 3 | [sw                                                           |
| - | - | atmf_pest_zon](https://github.com/spark-brc/swatmf_pest_zon), |
| J | J | donwloaded, install flopy and swatmf, check calibration       |
| u | u | example (**1 day**)                                           |
| n | n |                                                               |
|   |   | Add detail to the model: climate, groundwater parameters,     |
|   |   | modify model and build results (**2 days**)                   |
|   |   |                                                               |
|   |   | Talking with Sacha to start codes in python or R, the code    |
|   |   | should be able to modify swat files parameters to run         |
|   |   | multiple times (**½ day**)                                    |
|   |   |                                                               |
|   |   | Seonggyu Park email (files), and organize a meeting to solve  |
|   |   | questions. (**½ day**)                                        |
|   |   |                                                               |
|   |   | cedar vs douglas fir ET/growth and impacts on low flows (**1  |
|   |   | day**)                                                        |
+---+---+---------------------------------------------------------------+

**Videos**

C:\\Users\\auresy\\Documents\\Tutorial\\6 PEST\\Videos PEST

How to be more effective changing the data

Information

Links references

Create a table

Soil

SOIL UNITS: For Classification Key consult:
<http://www.fao.org/ag/agl/agll/key2soil.stm>

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name              Time   Resolution            Source
  ----------------- ------ --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  North America     2003                         <https://swat.tamu.edu/data/>
  SWAT soil                                      

  SOILS OF SOUTHERN 1985   Check for different   <https://www.env.gov.bc.ca/esd/distdata/ecosystems/Soils_Reports/bc44_report.pdf>
  VANCOUVER ISLAND         types of trees and    
                           soil, douglas fir,    
                           red cedar             

  Cordeiro et al.   2018   database for use in   <https://essd.copernicus.org/articles/10/1673/2018/>
                           SWAT simulations      

  The Canadian      1998                         <https://sis.agr.gc.ca/cansis/taxa/cssc3/index.html>
  System of Soil                                 
  Classification,                                
  3rd edition                                    

  FAO/UNESCO Soil   1979                         [document](https://www.fao.org/land-water/resources/publications/results/en/?page=2&ipp=10&no_cache=1&tx_dynalist_pi1[par]=YToxMDp7czoxOiJMIjtzOjE6IjAiO3M6NzoibXlfdHlwZSI7czowOiIiO3M6NToidGl0bGUiO3M6MDoiIjtzOjg6ImNhdGVnb3J5IjtzOjU6IjU1NTE0IjtzOjE2OiJzeXNfbGFuZ3VhZ2VfdWlkIjtzOjA6IiI7czo3OiJteV95ZWFyIjtzOjA6IiI7czoxNzoidHhfZHluYWZlZl9zZWFyY2giO3M6MToiMSI7czo3OiJyZWNfdWlkIjtzOjA6IiI7czoxMDoiYWN0X3NlYXJjaCI7czo2OiJTZWFyY2giO3M6MTM6ImZvcm1fYnVpbGRfaWQiO3M6Njk6ImZvcm0tNjJhMWNhNzM3ZjMzMmEzZDE1MzBmOTYxZGU3ZTc2OGZhODVhNjEzNGRmNDc0YjBmYTgyYzkwYjkzZWNmY2YwNyI7fQ==)
  Map of the                                     
  World - North                                  
  America                                        

  BC soil survey    2019                         <https://www.arcgis.com/home/item.html?id=127980379ea1446794902b02a8ca3c29>
  polygons                                       
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Evapotrasnpiration SWAT explanation:
<https://assets.researchsquare.com/files/rs-1201015/v1/c6e0c57c-d294-48d3-9134-ea7b5989e59c.pdf?c=1643649668>

Calculation of evapotranspiration

<file:///C:/Users/auresy/Downloads/etd8691_SFoster.pdf>

**Model development**

**DEM** resolution 30 x 30 m, do we have smaller? Is it good or do we
need to change the resolution?

**Soil**

Data Sources: **Lakes, Rivers** and Watersheds: Freshwater Atlas,
Ministry of FLNRORD, 2020 (link), **Soils**: Ministry of Climate Change,
2019. (link)

How to introduce lakes in SWAT? (information)

Anthropogenic, Colluvial, Fluvial, Fen-Peat, Glaciofluvial,
Glaciomarine, Marine, Till

BC Soil Information Finder Tool, Paper Canada SWAT soil

Compare paper with the BC soil information, how? Open it in arcgis?

**Land use** changes along the past, statistics

Compare maps, change HRUs or not, find the questions in the *group*
related to that

**Precipitation** distribution

Subbasin values of precipitation

**Temperature** distribution

Subbasin values of temperature

**K** distribution

**Biomass** function according to the years

**LAI** values

**Water use**

Add surface licenses (add points)

Observation

Modflow.obs
([link](https://groups.google.com/g/swat-modflow/c/lAUP4SFZ1ZM/m/zf5beluXAQAJ)
and detail information)

Streamflow.obs
([link](https://groups.google.com/g/swat-modflow/c/SmS7pgcGBjA))

**Calibration**

S. Park, review the program pest and create the files required for my
model

**Python**

Run multiple models with the code

Read

<https://www.tandfonline.com/doi/full/10.1080/02626667.2019.1590583>
