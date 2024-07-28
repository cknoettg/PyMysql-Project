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

    cursor.execute(f"SELECT user_name FROM {schema_name}.users WHERE user_id = {user_id}")

    # Close the connection
    cursor.close()
    conn.close()

# SQL logic for PUT request
def update_user(user_name):
    # trying with a singular case first
    user_id = 1
    new_user_name = "George"

    # SQL statement to UPDATE
    update_query = f"UPDATE {schema_name}.users SET user_name = %s WHERE user_id = %s"

    # Getting a cursor from Database
    cursor = conn.cursor()

    cursor.execute(update_query, (new_user_name, user_id))

    # Close the connection
    cursor.close()
    conn.close()

# SQL logic for DELETE request
def delete_user(user_name):
    # connect to DB and execute SQL statement
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {schema_name}.users WHERE name = user_name")
    # close the connection
    cursor.close()
    conn.close()
