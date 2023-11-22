import pandas as pd
import numpy as np
import subprocess as sp
import sqlalchemy as sqlalch
import opendatasets as od
from kaggle.api.kaggle_api_extended import KaggleApi
import os
import zipfile
import shutil
import sqlite3

command = 'kaggle datasets download -d merfarukgnaydn/last-2000-csgo-tournament-hltv/'

# Execute command
sp.run(command, shell=True)

zip_file_path = 'last-2000-csgo-tournament-hltv.zip'

extract_folder = 'last-2000-csgo-tournament-hltv'

# unzip zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# Path to the CSV file
csv_file_path = os.path.join(extract_folder, 'last2000tournament.csv')  

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Remove empty rows
df = df.dropna()  

data_folder = 'data' 

# Create the /data directory if it doesn't exist
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# SQLite database file path
sqlite_file = os.path.join(data_folder, 'last2000tournament.sqlite')

# Establish connection to database using sqlite
conn = sqlite3.connect(sqlite_file)

# Store DataFrame in the SQLite database
df.to_sql('last-2000-csgo-tournament-hltv', conn, index=False, if_exists='replace')

conn.close()

# Clean up
os.remove(zip_file_path)
shutil.rmtree(extract_folder)

#On top for first dataset and below for the second one

command = 'kaggle datasets download -d rankirsh/esports-earnings/'

# Execute command
sp.run(command, shell=True)

zip_file_path = 'esports-earnings.zip'

extract_folder = 'esports-earnings'

# unzip zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# Path to the CSV file
csv_file_path = os.path.join(extract_folder, 'GeneralEsportData.csv')  # Path to the CSV file

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Remove empty rows
df = df.dropna() 

data_folder = 'data' 

# SQLite database file path
sqlite_file = os.path.join(data_folder, 'GeneralEsportData.sqlite')

# Establish connection to database using sqlite
conn = sqlite3.connect(sqlite_file)

# Store DataFrame in the SQLite database
df.to_sql('esports-earnings', conn, index=False, if_exists='replace')

conn.close()

# Clean up
os.remove(zip_file_path)
shutil.rmtree(extract_folder)