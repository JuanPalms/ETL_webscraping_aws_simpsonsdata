import boto3
import awswrangler as wr
import os
from utility import load_config

glue = boto3.client('glue',region_name='us-east-1')
session = boto3.Session(profile_name='datascientist')
s3 = boto3.client('s3')


# Load config file calling load_config function
config_f = load_config("config.yaml")


query = '''
    CREATE TABLE IF NOT EXISTS simpsons.guests_per_episode AS (
        SELECT 
            a.season,
            a.episode_title,
            a.episode,
            a.viewer,
            b.guest_star,
            b.rol_himself_herself,
            b.guest
        FROM simpsons.seasons AS a
        LEFT JOIN simpsons.guests AS b
        ON a.season = b.season
        AND a.episode=b.episode
    )
'''

wr.athena.read_sql_query(query, database="simpsons", ctas_approach=False)

query = '''SELECT * FROM simpsons.guests_per_episode'''

tbl_guests_per_episode = wr.athena.read_sql_query(query, database="simpsons", ctas_approach=False)

tbl_guests_per_episode['guest'].fillna(0, inplace=True)
tbl_guests_per_episode['rol_himself_herself'].fillna(-1, inplace=True)
tbl_guests_per_episode['guest_star'].fillna("no_guest_star", inplace=True)


print(tbl_guests_per_episode)

tbl_guests_per_episode.to_csv(os.path.join(config_f["data_directory"]+config_f["clean_data"],"simpsons_analytics.csv"),index=False)
