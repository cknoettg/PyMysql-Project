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

if response.status_code == 200:
    print("User data successfully posted!")

    # Now make a GET request to verify the data
    get_response = requests.get(api_url)
    if get_response.status_code == 200:
        retrieved_data = get_response.json()
        # Compare retrieved_data with new_user_data
        print("Retrieved data:", retrieved_data)
    else:
        print("Error retrieving data:", get_response.status_code)
else:
    print("Error posting user data:", response.status_code)

