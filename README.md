# CISC4/667(-011): WebTips
This repository contains helpful script examples used in CISC 4/667-011 (Computing for Social Good) at the University of Delaware. The intention is to help make server and database interactions a bit easier and lightweight for course projects using ECE/CIS shared resources; however, students are welcome to use other tools if they choose.

## setup_script.py 
A Python script that will establish a simple SQLite database with a table and perform an insertion in the directory it is run in.

## server.py
A Python script that extends SimpleHTTPServer and establishes a server that will dynamically assign port numbers when executed and respond to specific GET requests. The service will function off the domain level URL using the port specified or 8080 if not. You must be using the VPN to access the service and you must ensure the service is running on the machine before it will be accessible.

## ping.py
A Python script example of a GET request.

## index.html
A JavaScript / JQuery page that will render the response from server.py to a GET request dynamically every 8 seconds.
