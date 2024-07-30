#import selenium
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# initialize the Chrome driver
driver = webdriver.Chrome()
# fetch the URL that displays a given user name
driver.get("http://127.0.0.1:5000/users/get_user_name/1")

# pause the browser to show that the user name element was selected
time.sleep(5)

try:
    # find the element with id 'user'
    user_name_element = driver.find_element(By.ID, value="user")
    # acknowledge that element exists
    print("User name element exists.")
    # print the found element
    user_name = user_name_element.text
    print(f"User name: {user_name}")
except NoSuchElementException:
    print("User name element does not exist.")