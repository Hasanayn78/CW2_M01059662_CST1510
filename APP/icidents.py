        
import pandas as pd

def migrate_cyber_incidents(conn):
    data=pd.read_csv('DATA/cyber_incidents.csv') # read from csv
    data.to_sql('cyber_inncident',conn)

def get_all_cyber_incidents(conn):
    sql = 'SELECT * FROM cyber_inncident'
    data = pd.read_sql(sql, conn)
    return data