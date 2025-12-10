def migrate_it_tickets(conn):
    data=pd.read_csv('DATA/it_tickets.csv') # read from csv
    data.to_sql('it_ticket',conn) #migrating the data