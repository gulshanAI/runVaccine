import requests
import time

while(True):
    response = requests.get('https://vaccinetouchmedia.herokuapp.com/')
    print("Called")
    print(response.status_code)
    print("Waiting for 30 seconds...")
    time.sleep(30)


# response = requests.get('https://vaccinetouchmedia.herokuapp.com/')
# print(response.status_code)