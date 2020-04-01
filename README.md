# Italy_Covid-19

## Introduction
In this repository i've collected some analysis written with Python on Covid-19 data for Italy. 
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
```

## Data
Data is taken from the following github repository as CSV files, which is updated daily:
(https://github.com/pcm-dpc/COVID-19)
Alternatively, data is directly imported in the jupyter notebook from the same repository above.

## Shapefiles
In order to plot geographic data i've also dowloaded shapefiles from the following site:

There are two mainly shape files: (http://www.diva-gis.org/gdata)

1. ***italy_regions.shp***: shapefile with regions of italy.
2. ***italy_provinces.shp***: shapefile with provinces of italy.

## Notebooks
Up to now I'm working on the following notebooks, saved in the src directory (code sources):

1. ***EDA.ipynb***: in this notebook there is a basic EDA, the codes are commented to understand the usage.

## Further Information

The aim of these analysis is simply to have a global view on behavior of Coronavirus in my country. Future goals are the development of predictive models in order to study and predict the behavior on the next days.


