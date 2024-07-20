import web_app
import db_connector
from flask import request

# POST logic
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_name):
    if request.method == 'GET':
        try:
            return {"status": "ok", "user_name": user_name}, 200
        except Exception as e:
            return 500


    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        return {'user id': user_id , 'user name': user_name}
  # todo elif for put and delete
# GET logic

# PUT logic

# DELETE logic
