# ETL television programs

This repository implements an ETL process using the data of the programs broadcasted in all the seasons of the show "The Simpsons". 

## Repository structure
```bash
.
├── config.yaml
├── data
│   └── raw # Stores scraped and wrangled data
│       ├── simpsons_episode_guests.csv 
│       └── simpsons_episodes_totals.csv
├── elt # Modules for Extract, Load, Transform steps
├── environment.yml # Provides libraries for replating this project
├── etl # Modules for Extract, Transform, Load steps
│   ├── extract_transform.py #Web scrapping and data wrangling
│   ├── load.py # Connection with S3 client and upload data to datalake
│   └── utility.py # Useful functions for etl steps
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
