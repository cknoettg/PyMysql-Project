from flask import Flask, request
from db_connector import add_user, get_user, update_user, delete_user

#create Flask app
app = Flask(__name__)

@app.route('/get_user_name', methods = ['GET'])
def get_user_name(user_id):
        user_name = get_user(user_id)
        if user_name == None:
                return "<H1 id='error'>" no such user: + user_id + "</H1>"
        else:
                return "<H1 id='user'>" + user_name + "</H1>"



app.run(host='127.0.0.1', debug=True, port=5000)
