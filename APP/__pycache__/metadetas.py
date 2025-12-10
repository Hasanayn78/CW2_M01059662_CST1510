import pandas as pd
import sqlite3



def migrate_dataset_metadetas(conn):
data_metadetas = pd.read_csv('DATA/datasets_metadata.csv')
data_metadetas.to_sql('datasets_metadata', conn)

def get_all_dataset_metadetas(conn):
sql = 'SELECT * FROM datasets_metadetas'
data = pd.read_sql(sql, conn)
df = pd.read_sql(sql, conn)
return data