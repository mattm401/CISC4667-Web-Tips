"""
ping.py
Example of a Get Request that returns some information
"""

import requests

x = requests.get('http://go.eecis.udel.edu:8081/api/v1/status/')
print(x.status_code)
print(x.content)
