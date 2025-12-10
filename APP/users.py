def add_user(conn,name,hash_password):
    curr = conn.cursor()
    sql= sql = "INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)"

    parram=(name, hash_password)
    curr.execute(sql,parram)
    conn.commit()

def migrate_users():
    conn.close()

    with open('DATA/users.txt','r') as f:
        users = f.readlines()

    for user in users:
        name,hash=user.strip().split(',')
        add_user(conn, name, hash)



def migrate_users():
    conn.close()

    with open('DATA/users.txt','r') as f:
        users = f.readlines()

    for user in users:
        name,hash=user.strip().split(',')
        add_user(conn, name, hash)
    conn.close()





def get_users():
    conn = sqlite3.connect('DATA/intelliget_platform.db')
    curr = conn.cursor()

    sql = "SELECT * FROM users"
    curr.execute(sql)
    users = curr.fetchall()

    conn.close()
    return users




def get_all_users(conn):
    curr=conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    param =('hasanayn',)
    curr.execute(sql,param)
    user= curr. fetchone()
    conn.close()
    print(user)