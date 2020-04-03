# Italy_Covid-19

## Introduction
In this repository I've collected some analysis written on Jupyter Notebook with Python about Covid-19 data for Italy. 
The structure of the repository is as follows:

```
Italy_Covid-19/
│
├── Data/
│   ├── national_trend.csv
│   ├── regions_trend.csv
│   ├── provinces_trend.csv
├── Shapefiles/
│   ├── regions/
│   │   ├── italy_regions.shp
│   │   ├── italy_regions.shx
│   │   ├── italy_regions.prj
│   │   ├── italy_regions.dbf
│   │   ├── italy_regions.cpg
│   ├── provinces/
│   │   ├── italy_provinces.shp
│   │   ├── italy_provinces.shx
│   │   ├── italy_provinces.prj
│   │   ├── italy_provinces.dbf
│   │   ├── italy_provinces.cpg
├── src/
│   ├── EDA.ipynb
│   ├── Forecasting.ipynb
│   ├── load_data.py
```
The jupyter notebooks have been built to work with the project structure above; specifically, once downloaded the repository one just needs to run jupyter and open the notebooks to start working.

## Data 
Data is directly imported in the jupyter notebook from the following github repository, which is the official one of Italian Civil Protection:
(https://github.com/pcm-dpc/COVID-19).

Data can be manually downloaded as CSV files from the latter and saved in the Data directory.

## Shapefiles
In order to plot geographic data i've also dowloaded shapefiles from the following site: (http://www.diva-gis.org/gdata)

There are two mainly shape files: 

1. ***italy_regions.shp***: shapefile with regions of italy.
2. ***italy_provinces.shp***: shapefile with provinces of italy.


## Notebooks
Up to now I'm working on the following notebooks, saved in the src directory (code sources):

1. ***EDA.ipynb***: in this notebook there is a basic EDA, the codes are commented to understand the usage.
                    In order to plot geographic data I've used geopandas package  (the official page suggests to create a specific  
                    virtual environment and install the geopandas dependencies there to avoid possible conflicts).
2. ***Forecasting.ipynb***: in this notebook i've tried to forecast the trend of total cases in each region. I've used:
   - Logistic model
                  

## Further Information

The aim of these analysis is simply to have a global view on behavior of Coronavirus in my country. Future goals are the enrinchment of predictive models in Forecasting notebook in order to study and predict the behavior on the next days. There are many difficulties related to this task:
- Little amount of historical data.
- Missing of important information such as exogenous variables (i.e. restriction policies and so on) and epidemiological variables characterizing virus spread in the actual dataset.

Anyway, I think it worths a try :)
Anyone who is interested in the analysis and has suggestions/hints about possible predictive models can write me to the following mail address: lorenzo92rota@gmail.com

## License
Data comes from various public sources, I believe that the results dataset can be classified under [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/
