#!/usr/bin/env python3


import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

directory = 'supplier-data/images/'
url = "http://[external-IP-address]/upload/"

for file in os.listdir(directory):
    if file.endswith('.jpeg'):
        f = os.path.join(directory, file)
        with open(f, 'rb') as opened:
            r = requests.post(url, files={'file': opened})