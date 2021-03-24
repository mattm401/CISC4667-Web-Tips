"""
ping.py
Example of a Get Request that returns some information
"""

import requests

x = requests.get('http://<ADD_URL>:8081/api/v1/status/')
print(x.status_code)
print(x.content)
