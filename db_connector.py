import pymysql

schema_name = "mydb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3378, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# SQL logic for POST request
def add_user(user_id, user_name, creation_date):

    # Getting a cursor from Database
    cursor = conn.cursor()

    cursor.execute(f"INSERT into {schema_name}.users (name, id, date) VALUES ('{user_name}', {user_id}, {creation_date})")

    # Close the connection
    cursor.close()
    conn.close()

# SQL logic for GET request
def get_user(user_id):
    # Getting a cursor from Database
    cursor = conn.cursor()

    cursor.execute(f"SELECT user_name FROM mydb.users WHERE id = {user_id}")

    # Close the connection
    cursor.close()
    conn.close()
