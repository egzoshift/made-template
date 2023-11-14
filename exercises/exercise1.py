import pandas as pd
import sqlalchemy as sqlalch

# column data types
types = {
    "column_1": sqlalch.INTEGER,
    "column_2": sqlalch.TEXT,
    "column_3": sqlalch.TEXT,
    "column_4": sqlalch.TEXT,
    "column_5": sqlalch.VARCHAR(3), #max 3 chars (string consisting of 3 chars)
    "column_6": sqlalch.VARCHAR(4),
    "column_7": sqlalch.FLOAT,
    "column_8": sqlalch.FLOAT,
    "column_9": sqlalch.INTEGER,
    "column_10": sqlalch.FLOAT,
    "column_11": sqlalch.CHAR(1),
    "column_12": sqlalch.TEXT,
    "geo_punkt": sqlalch.TEXT,
} 
### MAIN 

#header=0 -> first row contains column names, seperated by semicolons
csv_dataframe = pd.read_csv('https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv', sep=';', header=0)

# create SQLAlchemy engine pointing to the sqlite file
sqlite_file_engine = sqlalch.create_engine('sqlite:///airports.sqlite')


# use dataframe method to directly import it to the sqlite engine
csv_dataframe.to_sql('airports', con=sqlite_file_engine, 
                    if_exists='replace', # reruns possible since it just replaces the data -> no errors
                    dtype=types,
                    index=False) 