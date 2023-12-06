import sqlite3
import pandas as pd
import os

def check_data(table_name, path):
    con = sqlite3.connect(path)

    query = f"SELECT * FROM '{table_name}' LIMIT 3;"
    table_data = pd.read_sql_query(query, con)

    assert not table_data.empty, f"{table_name} data is empty."
    # assert primary_key_column in table_data.columns, f"{primary_key_column} column not found in {table_name} data."

    con.close()

def check_columns(table_name, expected_columns, path):
    con = sqlite3.connect(path)

    cur = con.cursor

    query = f"PRAGMA table_info('{table_name}');"
    #query2 = f"SELECT Game FROM '{table_name}'"
    #cur.execute(query2)
    table_info = pd.read_sql_query(query, con)

  
    missing_columns = set(expected_columns) - set(table_info['name'])
    wrong_columns = set(table_info['name']) - set(expected_columns)
    
    if wrong_columns or missing_columns:
        error_message = f"Columns mismatch in '{table_name}':\n"
        if wrong_columns:
            error_message = f"Unexpected columns: {', '.join(wrong_columns)}.\n"
        if missing_columns:
            error_message = f"Missing columns: {', '.join(missing_columns)}.\n"
        else: error_message = ""
    else: error_message = ""

    if error_message:
        raise AssertionError(error_message)
    con.close()

try:
    # General Esports Data
    check_columns('esports-earnings', ['Game', 'ReleaseDate', 'Genre', 'TotalEarnings', 'OfflineEarnings', 'PercentOffline', 'TotalPlayers', 'TotalTournaments'], os.path.join('data', 'GeneralEsportData.sqlite'))
    check_data('esports-earnings', os.path.join('data', 'GeneralEsportData.sqlite'))

    print("System test for Table GeneralEsportData worked.")

    # Last 2000 Tournaments
    check_columns('last-2000-csgo-tournament-hltv', ['Event Name', 'Location', 'Prize'], os.path.join('data', 'last2000tournament.sqlite'))
    check_data('last-2000-csgo-tournament-hltv', os.path.join('data', 'last2000tournament.sqlite'))

    print("System test for Table last2000tournament worked.")
    
except AssertionError as e:
    print(f"System test failed, reason: {e}")
    raise IOError("System test failed.") from e