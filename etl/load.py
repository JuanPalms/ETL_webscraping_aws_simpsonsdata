"""
This python module performs the Load Fase of the project. It uploads the data to the S3 Bucket of the project. 
"""
# Abres un cliente de S3
import os
from utility import load_config
import boto3
######### LOAD #######

# Load config file calling load_config function
config_f = load_config("config.yaml")
session = boto3.Session(profile_name='datascientist')
s3 = boto3.client('s3')

# Crea un nuevo Bucket
BUCKET_NAME = "itam-analytics-palmeros-1"
s3.create_bucket(Bucket=BUCKET_NAME)

# Upload los dos archivos a S3
s3.upload_file(Filename=os.path.join(config_f["data_directory"]+config_f["raw_data"],"simpsons_episode_guests.csv"),
               Bucket=BUCKET_NAME, Key="simpsons/raw/seasons/simpsons_episodios_totales.csv")
s3.upload_file(Filename=os.path.join(config_f["data_directory"]+config_f["raw_data"],"simpsons_episodes_totals.csv"),
               Bucket=BUCKET_NAME, Key="simpsons/raw/guests/simpsons_invitados.csv")