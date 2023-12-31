**Scientific notes**

Evapotranspiration

The model calculates evapotranspiration distributed spatially considering different rainfall patterns, land cover classification, and soil types. The method used is Penman-Monteith which considers variables such as canopy height, biomass, maximum depth root, and leaf area index. This is different from previous reports that uses temperature methods to calculate the evapotranspiration.

Groundwater

The model estimates the groundwater discharge and recharge, water moving from the aquifer to the river and from the river to aquifer according to the season and water availability. These results are compared with the information collected in the field by Kristina Disney during the summertime of the last 3 years.
The oldest images related to land cover are downloaded from Landsat satellite, first launched in 1972. Every two years these satellite images were taken improving the technology of the sensors with time. To read this information, it is necessary to separate the bands and to understand the type of information already in place to train the program to classify the land types.

Leaf Area Index

The Leaf Area Index (LAI) is a relevant parameter that in previous studies has been compared with satellite information. We observed that the LAI of Douglas Fir species (Sholes, 2023) is higher than the normal Evergreen Forest defined by SWAT. Also, the comparison with satellite information may have some problems considering there are multiple sources of error, that can lead to wrong reading of the LAI satellite information (for example the clouds, and the wet soil that can have a higher reflection and because of that could be considered as vegetation).

Canopy height

The canopy height was taken from research related to the sizes of Douglas Fir from different regions of West USA. The mean height for a Douglas Fir of 20 years old is 10.4 m (Petkova, 2011). However, if it is coastal Douglas Fir the elevation tends to be higher about 12 m. Similarly, a Douglas Fir of 60 years old has a height of 40 m. There are some aspects that are not considered from the trees in the model, for example the density of the tree's crops affects directly the growing. Douglas Fir was selected as the dominant species of the watershed considering different ages for the tree (20, 30 and 60 years old) as the management use to logged trees before 60 years old. These types are input in the crops archive QSWATRef2012.mdb.

Modification of parameters

The original parameters for evergreen forest are modified and adapted specifically to Douglas Fir are: maximum potential leaf area index (BLAI), fraction of the maximum leaf area index corresponding to the 1st and 2nd point on the optimal leaf area development curve (LAIMX1, LAIMX2), optimal temperature for plant growth (T_OPT), maximum canopy height (CHTMX), radiation-use efficiency (BIO_E), 2nd point on the radiation use efficiency curve (BIOEHI), rate of decline in radiation use efficiency per unit increase in vapor pressure deficit (WAVP), elevated CO2 atmospheric concentration (CO2HI), maximum stomatal conductance at high solar radiation and low vapor pressure deficit (GSI), number of years required for tree species to reach full development (MAT_YRS), maximum biomass for a forest (BMX_TREES), maximum root depth (RDMX), fraction of tree biomass accumulated each year that is converted to residue during dormancy (BIO_LEAF), and minimum leaf area index for plant during dormant period (ALAI_MIN), values modified from (Mueller-Warrant et al., 2019)

Climate

The climate input for SWAT model considers the closest hydrometeorological stations that are located in Shawnigan Lake and Cowichan Lake (no data values are set up to -99). These stations have records of precipitation and temperature from 1960. Considering the map, they are in the north-west and south-east. There is no wind speed, relative humidity and solar radiation as close as the other variables. However, these variables were taken from a station in Nanaimo. There is a program called WGEN used to generate the statistics of climate variables. Each subbasin uses specific interpolated values from these variables to perform calculation of the hydrologic cycle.
The water use is specified in a file in the 12 months of a year for all reaches, shallow and depth aquifers. 
After having this information SWAT uses slope, soil, and land use to create what are called Hydrologic Response Units or HRUs. Which are subareas in the subbasins. There are 197 subbasins with around 2000 HRUs in the model.

SWAT groundwater 

Using SWAT (alone), the groundwater part of the model is divided into two aquifer systems: the shallow unconfined aquifer, which returns flow to the streams, and the deep aquifer, which does not return flow to the streams. The parameters considered for groundwater movement are (1) groundwater delay (days), GW_DELAY, (2) baseflow alpha factor (days) ALPHA_BF, (3) threshold depth of water in the shallow aquifer required for return flow to occur (mm) GWQMN, (4) groundwater "revap" coefficient, GW_REVAP, (5) threshold depth of water in the shallow aquifer for "revap" to occur (mm), REVAPMN, (6) deep aquifer percolation fraction, RCHRG_DP. The obtained values by the calibration of the model explain groundwater characteristics, for example, the time the water needs to move between layers, which is related to the hydraulic properties of the aquifers. The water can be infiltrated (downward movement) and evaporated (diffusion upward). Also, water can be absorbed by plant roots. We use similar values for GW_REVAP and REVAPMN in all watershed subbasins. However, these parameters can be modified according to land use and soil characteristics. After one year of simulation for preparing calibration, the system equilibrates the water cycle, which initially had 1m and 2 m water depths for the shallow and deep aquifers, respectively. 

Sensitivity

To analyze sensitivity after calibration, we use the t-stat measures how accurately a regression coefficient is estimated by dividing the coefficient of a parameter by its standard error. We compare a coefficient to its standard error to determine whether it differs significantly from zero. We can infer that the parameter is sensitive when the coefficient is "large" compared to its standard error.
The p-value tests the null hypothesis for each term, where the coefficient equals zero, indicating no effect. Low p-values mean that we can reject the null hypothesis and consider the predictor statistically significant. In other words, a predictor with a low p-value is likely to contribute meaningfully to the model because changes in the predictor's value are associated with changes in the response variable. On the other hand, a larger p-value shows that changes in the response are not associated with changes in the predictor so that parameter is not very sensitive.

_____________________________________________________________
Parts in progress for the SWAT-MODFLOW model

MODFLOW model is based on previous information about aquifers in this area. The aquifers have wells with information of bedrock and the lowest points to obtain groundwater. There are around 1600 wells with different pumping rates. The pumping rates were changed to international units and organized with python to enter pumping schedule in the .gpt file of the model considering the programing format of Delphi.
Once these two models are organized separately, they are joined using SWAT-MODFLOW. The connection of the discretized cells and the HRUs. The plugin interface created for QGIS was useful to ensemble some of the first models. Later in order to have multiple runs the program was run using cmd command prompt.
The model used for calibration and validation was from 2008-2018 and 2019-2022. This period was chosen because it has dynamic groundwater levels recorded in at least two points located in the same place but in a different depth. Later from 2019, there are 2 additional observation wells that are integrated for the validation period. This process used PEST and a code created for calibration in Jupyter (python). There are files related to the observed information to compare with multiple simulated results and define the sensitivity of the parameters selected or calibration. 
