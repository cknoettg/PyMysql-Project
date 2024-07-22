import web_app
import db_connector
import requests
from flask import request

# Create route for each REST API method
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_name):
    # GET logic
    if request.method == 'GET':
        try:
            res = requests.get('http://127.0.0.1:5000/data/{user_id}')
            request_data = res.json
            user_id = request_data['user_id']
            cursor = db_connector.conn.cursor()
            cursor.execute(f"SELECT user_name FROM mydb.users WHERE id = {user_id}")
            cursor.close()
            db_connector.conn.close()
            return {"status": "ok", "user_name": user_name}, 200
        except Exception as e:
            return 500

    # POST logic
    elif request.method == 'POST':
        try:
            # Getting the json data payload from request
            request_data = request.json

            # Formatting the POST request
            user_id = request_data['user_id']
            user_name = request_data['user_name']
            creation_date = request_data['creation_date']

            # Treating request_data as a dictionary to get a specific value from key
            # user_name = request_data.get("user_name")

            # Create cursor, then execute the POST SQL statement
            cursor = db_connector.conn.cursor()
            cursor.execute(f'INSERT INTO mydb.users (user_id, user_name, creation_date) VALUES (%s, %s, %s)',
                           (user_id, user_name, creation_date))

            return {"status": "ok", "user_added": user_name}, 200
        except Exception as e:
            return {"status": "error", "reason": "id already exists"}, 500

    # PUT logic
    elif request.method == 'PUT':
        try:
            user_id = 1
            new_user_name = "George"

            update_query = f"UPDATE users SET user_name = %s WHERE = %s"

            cursor = db_connector.conn.cursor()
            cursor.execute(update_query, (new_user_name, user_id))
            cursor.close()
            db_connector.conn.close()
            return {"status": "ok", "user_updated": user_name}, 200
        except Exception as e:
            return {"status": "ok", "reason": "no such id"}, 500

    # DELETE logic
    elif request.method == 'DELETE':
        try:
            res = requests.get('http://127.0.0.1:5000/data/{user_id}')
            request_data = res.json
            user_id = request_data['user_id']
            user_name = request_data['user_name']
            cursor = db_connector.conn.cursor()

            cursor.execute(f"DELETE FROM mydb.users WHERE name = 'user_name'")

            cursor.close()
            db_connector.conn.close()
            return {"status": "ok", "user_deleted": user_id}, 200
        except Exception as e:
            return {"status": "error", "reason": "no such id"}, 500
