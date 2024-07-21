import web_app
import db_connector
from flask import request

# Create route for each REST API method
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_name):
    # GET logic
    if request.method == 'GET':
        try:
            return {"status": "ok", "user_name": user_name}, 200
        except Exception as e:
            return 500

    # POST logic
    elif request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get("user_name")
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
            return {"status": "ok", "user_updated": user_name}, 200
        except Exception as e:
            return {"status": "ok", "reason": "no such id"}, 500

# DELETE logic
