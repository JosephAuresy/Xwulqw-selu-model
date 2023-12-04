**DEM**

**Data source**: USGS\
**Persistent web-link**: <https://earthexplorer.usgs.gov>\
**Temporal range**: NA\
**Spatial resolution**: 30x30 m\
**Description and justification**. This data is used for SWAT initial inputs\
**Preprocessing**: QGIS\

**Soil**

**Data source:** Cordeiro et al. (2018)\
**Persistent web-link**:
<https://doi.pangaea.de/10.1594/PANGAEA.877298>\
**Temporal range**: NA\
**Spatial resolution**: NA\
**Description and justification**: This database has the parameters from
Soils of Canada adapted in a format ready to be used in SWAT
simulations. Out of the 14,063 unique soils in the SLC, 11,838 soils
with complete information\
**Preprocessing**: Revise the soils that are not classified due to the
lack of information and finding the closest group for them to add the
parameters in SWAT with Access.\

**Land use**

**Data source**: AAFC Land Use\
**Persistent web-link**: <https://open.canada.ca/data/en/dataset/fa84a70f-03ad-4946-b0f8-a3b481dd5248>\
**Temporal range**: 2000-2020\
**Spatial resolution**: 30x30 m\
**Description and justification**: The land use classes follow the protocol of the Intergovernmental Panel on Climate Change (IPCC) with further differentiation within some classes\
**Preprocessing**: NA\

**Climate**

**Precipitation and Temperature**
**Data source**: Government of Canada\
**Persistent web-link**: <https://climate.weather.gc.ca>\
**Temporal range**: 1950-2022\
**Spatial resolution**: NA\
**Description and justification**. This information is used as input for the program WGN\
**Preprocessing**: Filling no data with -99 to interpolate with other stations\
**Preprocessing script**: <https://github.com/JosephAuresy/Xwulqw-selu-model/blob/main/Climate>\

**Solar radiation, relative humidity and wind speed**

**Data source**: Funk et al. (2014)\
**Persistent web-link**: <https://swat.tamu.edu/data/chirps-chirts/>\
**Temporal range**: 1979-2014\
**Spatial resolution**: NA\
**Description and justification**: Climate Hazards Group Infrared Precipitation with Stations (CHIRPS).\
**Preprocessing**: NA\

**Wells and Pumping**

**Data source**: British Columbia, Groundwater Wells and Aquifers\
**Persistent web-link**: <https://apps.nrs.gov.bc.ca/gwells/>\
**Temporal range**: NA\
**Spatial resolution**: NA\
**Description and justification**: Information related to well depth, location, pumping rate, etc.\
**Preprocessing**: Organization of wells by aquifer\
**Preprocessing script**: <https://github.com/JosephAuresy/Xwulqw-selu-model/tree/main/Pumping>
