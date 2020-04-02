import pandas as pd
import geopandas as gpd
import os
import numpy as np


def load_covid_data(DATA_DIR = ''):
    
    if DATA_DIR == '':
        # Italy data: url to github repository of Civil Protection
        url_national = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
        url_regions = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv'
        url_provinces = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv'
        
        # load data
        data_provinces = pd.read_csv(url_provinces, error_bad_lines=False)
        data_regions = pd.read_csv(url_regions, error_bad_lines=False)
        data_national = pd.read_csv(url_national, error_bad_lines=False)
        
    else:
        
        filename_provinces = os.path.join(DATA_DIR, '.csv')
        filename_regions = os.path.join(DATA_DIR, '.csv')
        filename_national = os.path.join(DATA_DIR, '.csv')
        
        data_provinces = pd.read_csv(filename_provinces)
        data_regions = pd.read_csv(filename_regions)
        data_national = pd.read_csv(filename_national)
    
    return data_provinces, data_regions, data_national
    
def load_shapefiles(SHAPEFILES_DIR):
    
    
    filename_regions = os.path.join(SHAPEFILES_DIR,'regions/italy_regions.shp')
    italy_regions = gpd.read_file(filename_regions)
    
    filename_provinces = os.path.join(SHAPEFILES_DIR,'provinces/italy_provinces.shp')
    italy_provinces = gpd.read_file(filename_provinces)
    
    # map  ID from shapefiles with covid data
    changing_names, _, _ = dictionary_creation()
    
    # changing region names in italian
    italy_regions['NAME_1'] = italy_regions['NAME_1'].map(changing_names)
    
    # changing region names in italian 
    italy_provinces['NAME_1'] = italy_provinces['NAME_1'].map(changing_names)
    
    return italy_provinces, italy_regions

def dictionary_creation():
    
    """
    This function returns three dictionaries used to map information between shape files and Covid-19 data
    """
    
    # dictionary to change region names in italian for shape files
    changing_names = {'Abruzzo': 'Abruzzo', 'Basilicata': 'Basilicata', 'Calabria': 'Calabria', 
                  'Campania': 'Campania', 'Emilia-Romagna': 'Emilia-Romagna',
                  'Friuli-Venezia Giulia': 'Friuli Venezia Giulia', 'Lazio': 'Lazio', 
                  'Liguria': 'Liguria', 'Lombardia': 'Lombardia', 'Marche': 'Marche',
                  'Molise': 'Molise', 'Trentino-Alto Adige': 'Trentino Alto Adige', 'Piemonte': 'Piemonte',
                  'Apulia': 'Puglia', 'Sardegna': 'Sardegna', 'Sicily': 'Sicilia', 'Toscana': 'Toscana',
                  'Umbria': 'Umbria', "Valle d'Aosta": "Valle d'Aosta", 'Veneto': 'Veneto'}
    
    # dictionary to map regions id of shape files in geodataframe of regions
    dictionary_regions = {'Abruzzo': 1, 'Basilicata': 3, 'Calabria': 4, 'Campania': 5, 'Emilia-Romagna': 6,
                     'Friuli Venezia Giulia': 7, 'Lazio': 8, 'Liguria': 9, 'Lombardia': 10, 'Marche': 11,
                     'Molise': 12, 'P.A. Bolzano': 17, 'P.A. Trento': 17, 'Piemonte': 13, 'Puglia': 2, 'Sardegna': 14,
                     'Sicilia': 15, 'Toscana': 16, 'Umbria': 18, "Valle d'Aosta": 19, 'Veneto': 20} 
    
    # dictionary to map provinces id of shape files in geodataframe of regions
    dictionary_provinces = {'Agrigento': 80, 'Alessandria': 64, 'Ancona': 57, 'Aosta': 103, 'Arezzo': 89, 'Ascoli Piceno': 58,
                       'Asti': 65, 'Avellino': 18, 'Bari': 5, 'Barletta-Andria-Trani': 6, 'Belluno': 104, 'Benevento': 19,
                       'Bergamo': 45, 'Biella': 66, 'Bologna': 23, 'Bolzano': 99, 'Brescia': 46, 'Brindisi': 7, 'Cagliari': 72,
                       'Caltanisetta': 81, 'Campobasso': 62, 'Caserta': 20, 'Catania': 82, 'Catanzaro': 13, 'Chieti': 1,
                        'Como': 47, 'Cosenza': 14, 'Cremona': 48, 'Crotone': 15, 'Cuneo': 67, 'Enna': 83, 'Fermo': 59, 'Ferrara': 24,
                        'Firenze': 90, 'Foggia': 8, 'Forlì-Cesena': 25, 'Frosinone': 36, 'Genova': 41, 'Gorizia': 32, 
                        'Grosseto': 91, 'Imperia': 42, 'Isernia': 63, "L'Aquila": 2, 'La Spezia': 43, 'Latina': 37, 'Lecce': 9,
                       'Lecco': 49, 'Livorno': 92, 'Lodi': 50, 'Lucca': 93, 'Macerata': 60, 'Mantova': 51, 'Massa Carrara': 94,
                        'Matera': 11, 'Messina': 84, 'Milano': 52, 'Modena': 26, 'Monza e della Brianza': 53, 'Napoli': 21,
                        'Novara': 68, 'Nuoro': 75, 'Oristano': 78, 'Padova': 105, 'Palermo': 85, 'Parma': 27, 'Pavia': 54,
                        'Perugia': 101, 'Pesaro e Urbino': 61, 'Pescara': 3, 'Piacenza': 28, 'Pisa': 95, 'Pistoia': 96,
                        'Pordenone': 33, 'Potenza': 12, 'Prato': 97, 'Ragusa': 86, 'Ravenna': 29, 'Reggio di Calabria': 16,
                        "Reggio nell'Emilia": 30, 'Rieti': 38, 'Rimini': 31, 'Roma': 39, 'Rovigo': 106, 'Salerno': 22, 'Sassari': 79,
                        'Savona': 44, 'Siena': 98, 'Siracusa': 87, 'Sondrio': 55, 'Sud Sardegna': np.nan, 'Taranto': 10, 'Teramo': 4,
                        'Terni': 102, 'Torino': 69, 'Trapani': 88, 'Trento': 100, 'Treviso': 107, 'Trieste': 34, 'Udine': 35, 
                        'Varese': 56, 'Venezia': 108, 'Verbano-Cusio-Ossola': 70, 'Vercelli': 71, 'Verona': 109, 'Vibo Valentia': 17,
                        'Vicenza': 110, 'Viterbo': 40} 
    
    return changing_names, dictionary_regions, dictionary_provinces