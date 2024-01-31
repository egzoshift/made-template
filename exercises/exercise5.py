import urllib.request
import pandas as pd
import zipfile
import os
from sqlalchemy import create_engine, types

def download_data():
    source = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
    file = "stops.txt"
    tmpDir = "exercise5"
    tmpFile = "exercise5.zip"

    urllib.request.urlretrieve(source, tmpFile)
    with zipfile.ZipFile(tmpFile, 'r') as zip:
        zip.extractall(tmpDir)

    return os.path.join(tmpDir, file)


def load_data(path):
    cols = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]
    df = pd.read_csv(path, sep=",", encoding="utf-8", usecols=cols)
    return df

def store_data(df):
    sql_dtype = {
        'stop_id': types.INT,
        'stop_name': types.TEXT,
        'stop_lat': types.FLOAT,
        'stop_long': types.FLOAT,
        'zone_id': types.INT,
    }

def transform_data(df):
    return df.query("(zone_id == 2001) and (-90 <= stop_lat <= 90) and (-90 <= stop_lon <= 90)")



    engine = create_engine('sqlite:///gtfs.sqlite', echo=False) 
    df.to_sql(name='stops', con=engine, index=False, if_exists='replace', dtype=sql_dtype)
    engine.dispose()


def main():
    path = download_data()
    df = load_data(path)
    df = transform_data(df)
    store_data(df)


if __name__ == "__main__":
    main()
