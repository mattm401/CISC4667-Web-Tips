"""
ping.py
Example of a Get Request that returns some information
"""

import requests
import json

domain = "localhost"
port = 8080

x = requests.get('http://' + domain + ':' + str(port) + '/api/v1/status/')
print("Get Request Completed with Status - Message: " + str(x.status_code) + " - "
      + str(json.loads(x.content)['message']))

data = {'message': 'This is an example POST request'}
x = requests.post('http://' + domain + ':' + str(port) + '/', json=data)
print("Post Request Completed with Status: " + str(x.status_code))
