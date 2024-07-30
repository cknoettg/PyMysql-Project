import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By

schema_name = "mydb"

# Define the REST API URL
api_url = "http://127.0.0.1:5000/users/<user_id>"

# Define JSON data to POST
new_user_data = {
    "user_id": 5,
    "user_name": "thomas",
    "creation_date": "7-29-2024"
}

# Send a POST request
response = requests.post(api_url, json=new_user_data)
# Handle exceptions
if response.status_code != 200:
    raise Exception("Test failed: POST request failed")

# Extract user ID from the API response
user_id = response.json().get("user_id")

# Make a GET request to verify data
get_response = requests.get(api_url)
if get_response.status_code != 200:
    raise Exception("Test failed: GET request failed")
