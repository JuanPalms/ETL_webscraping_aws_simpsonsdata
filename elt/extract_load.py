"""
This python module perfoms the extraction phase of the project from an S3 bucket,
it 
"""
import boto3
import awswrangler as wr
#Crear una base de datos en el Glue Catalog
glue = boto3.client('glue',region_name='us-east-1')
session = boto3.Session(profile_name='datascientist')
s3 = boto3.client('s3')

#Create a database
#response = glue.create_database(
 #   DatabaseInput={
  #      'Name': 'simpsons',
   #     'Description': 'Simpsons season and episodes database.',
    #}
#)

# create queries bucket
#s3.create_bucket(Bucket="itam-athena-queries-palmeros")

## a) Extract y b) Load
#Season Guests Table

query = '''
    CREATE EXTERNAL TABLE IF NOT EXISTS `simpsons`.`guests` (
    `season` smallint,
    `guest_star` string,
    `episode_title` string,
    `rol_himself_herself` smallint,
    `episode` smallint,
    `guest` smallint
    ) COMMENT "Catalog of guests in Simpsons Episodes."
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
    WITH SERDEPROPERTIES ('field.delim' = ',')
    STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
    LOCATION 's3://itam-analytics-palms/simpsons/raw/seasons/'
    TBLPROPERTIES ('classification' = 'csv', "skip.header.line.count"="1");
'''

wr.athena.read_sql_query(query, database="simpsons", ctas_approach=False)

# Episodes table

query = '''
    CREATE EXTERNAL TABLE IF NOT EXISTS `simpsons`.`seasons` (
    `no_overall` smallint,
    `episode` smallint,
    `episode_title` string, 
    `directed_by` string, 
    `written_by` string,
    `date_aired` timestamp, 
    `household_or_viewers` string, 
    `season` smallint,
    `viewer` float,
    `viewer_units` string
    ) COMMENT "Catalog of Simpsons episodes."
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
    WITH SERDEPROPERTIES ('field.delim' = ',')
    STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
    LOCATION 's3://itam-analytics-palms/simpsons/raw/guests/'
    TBLPROPERTIES ('classification' = 'csv', "skip.header.line.count"="1");
'''

wr.athena.read_sql_query(query, database="simpsons", ctas_approach=False)
