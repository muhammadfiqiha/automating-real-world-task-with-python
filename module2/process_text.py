#!/usr/bin/env python3

import os
import requests

# define the directory and url
src_directory = '/data/feedback'
url = "http://<corpweb-external-IP>/feedback/"

# for loop to list all files in src_directory
for file in os.listdir(src_directory):
    # get the file path
    f = os.path.join(src_directory, file)
    with open(f) as texts:
        lines = texts.readlines()
        # create the dictionary request based on file content
        request_dict = {
            "title": lines[0].strip('\n'),
            "name": lines[1].strip('\n'),
            "date": lines[2].strip('\n'),
            "feedback": lines[3].strip('\n')
        }
        # upload the dictionary
        res = requests.post(url, json=request_dict)

        # raise error if status code not 201
        if res.status_code != 201:
            res.raise_for_status()