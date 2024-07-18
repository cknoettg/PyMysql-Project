from flask import Flask, request

#create Flask app
app = Flask(__name__)

app.run(host='127.0.0.1', debug=True, port=5000)
