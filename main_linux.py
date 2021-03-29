import pandas as pd 
import numpy as np 
import sqlite3
from sqlite3 import Error

#load csv data
def load_data(path):
    df = pd.read_csv(path, sep = " ", names = ["TYPE","START", "SEP","END","SEP2","ACTION"], parse_dates = ["START","END"], date_parser= lambda col:pd.to_datetime(col).strftime("%Y-%m-%dT%H:%M:%SZ"))
    df["DIFF"] = df["END"] - df["START"]
    return df
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def insert_rows(conn, df):
    """
    Create a new project into the projects table
    :param conn:
    :param dataframe_df:
    :return: last_row_id
    """
    cur = conn.cursor()
    sql =  ''' INSERT INTO summary (START,END,ACTION,DIFF)
              VALUES(?,?,?,?) '''
    [cur.execute(sql,(str(row['START']),str(row['END']),row['ACTION'],str(row['DIFF']))) for idx, row in df.iterrows()]
    conn.commit
def main():
    database = r"/mnt/D/timew-extensions/timew.db"
    sql_create_summary_table = """CREATE TABLE IF NOT EXISTS summary  (
	"START"	TEXT,
	"END"	TEXT,
	"ACTION"	TEXT,
	"DIFF"	TEXT
    );"""
    conn = create_connection(database)
    if conn is not None:
        create_table(conn,sql_create_summary_table)
    else:
        print("Error Cannot Connect to database")
    df = load_data("data.txt")
    with conn:
        insert_rows(conn, df)
if __name__ == '__main__':
    main()

