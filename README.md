# ETL television programs

This repository implements an ETL process using the data of the programs broadcasted in all the seasons of the show "The Simpsons". 

## Repository structure
```bash
├── config.yaml
├── data
│   └── raw
│       └── simpsons_episode_guests.csv
├── environment.yml
├── README.md
├── requirements.txt
└── src
    ├── extract_transform.py
    └── utility.py
```
## Data

The list of "The Simpsons" episodes season (1-20)
Available at: 
https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_1_(1989%E2%80%9390)



## Working environment

The working environment of this project can be recreated using a conda environment or via pip installation. For that purpose the files "environment.yml" and "requirements.txt" are provided.
