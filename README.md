# ETL television programs

This repository implements an ETL process using the data of the programs broadcasted in all the seasons of the show "The Simpsons". 

## Repository structure
```bash
ETL_ELT_SIMPSONS_PROJECT
├── analytics
│   ├── EDA.ipynb  # Python notebook that displays the final analytics of the simpsons seasons.
│   └── utility.py # Useful functions for analytics steps
├── config.yaml # defines global parameters to be invoked along the project/
├── data
│   ├── clean
│   │   └── simpsons_analytics.csv # Web scrapped complete data to be stored in data warehouse
│   └── raw
│       ├── simpsons_episode_guests.csv # Web scrapped data for further processing
│       └── simpsons_episodes_totals.csv # Web scrapped data for further processing
├── elt # Modules for Extract, Load, Transform steps
│   ├── extract_load.py # Datawarehouse creation in a S3 bucket
│   ├── transform_analytics.py # SQL queries in order to extract usefull data for analytics
│   └── utility.py
├── environment.yml # Provides libraries for replicating this project
├── etl #
│   ├── extract_transform.py  # Web scrapping process with pandas parser
│   ├── load.py  # Datalake creation in a S3 bucket
│   └── utility.py
├── README.md
└── requirements.txt



```
## Data

The list of "The Simpsons" episodes season (1-20)
Available at: 
https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_1_(1989%E2%80%9390)



## Working environment

The working environment of this project can be recreated using a conda environment or via pip installation. For that purpose the files "environment.yml" and "requirements.txt" are provided.

You can replicate the project environment by using a conda environment:

``` bash
conda env create --file environments.yml
```
