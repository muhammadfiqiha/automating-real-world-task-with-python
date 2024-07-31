#!/usr/bin/env python3

import os
import requests

src_directory = 'supplier-data/descriptions/'
url = "http://<external-IP>/feedback/"

for file in os.listdir(src_directory):
    f = os.path.join(src_directory, file)
    with open(f) as texts:
        lines = texts.readlines()
        file_basename = os.path.splitext(os.path.basename(f))[0]
        
        request_dict = {
            "name": lines[0].strip('\n'),
            "weight": int(lines[1].strip(' lbs\n')),
            "description": lines[2].strip('\n'),
            "image_name": file_basename + '.jpeg'
        }
        
        res = requests.post(url, json=request_dict)

        if res.status_code != 201:
            res.raise_for_status()