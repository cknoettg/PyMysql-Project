import requests
import pymysql

# Define the REST API URL
api_url = "http://127.0.0.1:5000/users/<user_id>"

# Define JSON data to POST
new_user_data = {
    "user_id": 4,
    "user_name": "greg",
    "creation_date": "7-29-2024"
}

# Send a POST request
response = requests.post(api_url, json=new_user_data)



