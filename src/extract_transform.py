"""
This python module performs the data extraction step of the project using web scraping with the pandas parser.
"""
import pandas as pd
import numpy as np
import os
from utility import load_config
######### EXTRACT #########
# Episodes data

# Load config file calling load_config function
config_f = load_config("config.yaml")

PATH_episodes="https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_1_(1989%E2%80%9390)"

#Reads html with pandas parser
tbls_raw_simpsons_episodes=pd.read_html(PATH_episodes)

#Drop unwanted data (we keep the data per episode for 20 seasons)
tbls_raw_simpsons_episodes=tbls_raw_simpsons_episodes[1:22]

#Guest per episode data
PATH_guest="https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars_(seasons_1%E2%80%9320)"

#Reads html with pandas parser
tbls_raw_simpsons_guests=pd.read_html(PATH_guest)

#Drop unwanted data (we keep the data per episode for 20 seasons)
tbls_raw_simpsons_guests=tbls_raw_simpsons_guests[1]
# Drop data about 2007 movie
tbls_raw_simpsons_episodes=tbls_raw_simpsons_episodes[0:18]+tbls_raw_simpsons_episodes[19:21]

######## TRANSFORM ##########

##### GUEST PER EPISODE

# Define un diccionario con los nombres limpios
DICT_CLEAN_NAMES_GUESTS_TABLE = {
    'Season': 'season',
    'Guest star': 'guest_star',
    'Role(s)': 'roles',
    'No.': 'no',
    'Prod. code': 'prod_code',
    'Episode title': 'episode_title'
}

# Transformacion de las columnas


# Aqui va el preprocesamiento
tbl_guests_per_episode_raw = (
    tbls_raw_simpsons_guests
        # Renombrar variables
        .rename(columns = DICT_CLEAN_NAMES_GUESTS_TABLE)
        # Drop undesired columns
        .drop(columns='prod_code')
        # Extraer el numero de episodio
        .assign(
            episode = lambda df_: df_['no'].str.extract(r'(\d{2})$'),
            episode_title = lambda df_: df_.episode_title.str.replace(r'([[0-9]*])', "", regex=True).str.replace('"', ''),
            rol_himself_herself = lambda df_: (df_['roles'] == 'Himself') | (df_['roles'] == 'Herself'))
        #Change datatype columns for appropiate merge
        .assign(
            rol_himself_herself=lambda df_: df_['rol_himself_herself'].astype(int),
            #episode=lambda df_: df_['episode'].astype(int),
            #season=lambda df_: df_['season'].astype(int)
            )
        # Elimino la columna no
        .drop(columns=['no','roles'])
)
print(tbl_guests_per_episode_raw.head())
# Guarda los datos en local
tbl_guests_per_episode_raw.to_csv(os.path.join(config_f["data_directory"]+config_f["raw_data"],"simpsons_episode_guests.csv"),index=False)

###### EPISODES SEASONS 1-20

# Define un diccionario con los nombres limpios

DICT_CLEAN_NAMES_EPISODES_TABLE = {
    'No. overall': 'no_overall',
    'No. in season': 'no',
    'Title': 'title',
    'Directed by': 'directed_by',
    'Original air date': 'date_aired',
    'Prod. code': 'prod_code',
    'U.S. viewers (millions)': 'household_or_viewers',    
}

# Adding season numbers and getting all together in a single table
episodes_df=pd.DataFrame()
for tbl_index in np.arange(0,20, 1):
    tbls_raw_simpsons_episodes[tbl_index]['season']=tbl_index+1
    episodes_df = pd.concat([episodes_df,tbls_raw_simpsons_episodes[tbl_index]])

#Modify index of resulting dataframe
episodes_df.set_index('No. overall', inplace=True)

print(episodes_df.tail())

