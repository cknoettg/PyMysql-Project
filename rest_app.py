#import web_app
#import db_connector
import requests
from datetime import datetime
from flask import Flask, request
from db_connector import add_user, get_user, update_user, delete_user

app = Flask(__name__)

# Create route for each REST API method
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    # GET logic
    if request.method == 'GET':
        try:
            # fetch data from path
            request_data = request.json
            user_id = request_data['user_id']
            user_name = request_data['user_name']

            # fetch user
            get_user(user_id)

            return {"status": "ok", "user_name": user_name}, 200
        except Exception as e:
            return {"status": "error", "reason": "no such id"}, 500

    # POST logic
    elif request.method == 'POST':
        try:
            # Getting the json data payload from request
            request_data = request.json

            # Formatting the POST request
            user_id = request_data['user_id']
            user_name = request_data['user_name']
            creation_date = request_data['creation_date']

            # test to see if correct data was sent - worked
            # print(request_data)
            # Treating request_data as a dictionary to get a specific value from key
            # user_name = request_data.get("user_name")

            # trying with a singular case first - worked
            # add_user(1, "john", datetime.now())

            # Genericizing the request
            add_user(user_id, user_name, creation_date)

            return {"status": "ok", "user_added": user_name}, 200
        except Exception as e:
            return {"status": "error", "reason": "id already exists"}, 500

    # PUT logic
    elif request.method == 'PUT':
        try:
            # trying with a singular case first
            #user_id = 1
            #new_user_name = "George"

            # fetch user name and id
            request_data = request.json
            user_id = request_data['user_id']
            user_name = request_data['user_name']

            # test to see if output is right - works
            # print(request_data)

            update_user("john")

            return {"status": "ok", "user_updated": user_name}, 200
        except Exception as e:
            return {"status": "ok", "reason": "no such id"}, 500

    # DELETE logic
    elif request.method == 'DELETE':
        try:
            # get user id and user name to delete
            res = requests.get('http://127.0.0.1:5000/users/{user_id}')
            request_data = res.json
            user_id = request_data['user_id']
            user_name = request_data['user_name']

            # trying with singular case first
            delete_user("George")

            return {"status": "ok", "user_deleted": user_id}, 200
        except Exception as e:
            return {"status": "error", "reason": "no such id"}, 500

app.run(host='127.0.0.1', debug=True, port=5000)
