#!/usr/bin/env python3

import os
from PIL import Image

# define the directory
directory = './images'

## for loop to get list of file from directory
for file in os.listdir(directory):
  # process if there is not .DS_Store in file
  if '.DS_Store' not in file:
    f = os.path.join(directory + '/', file) # get the file path
    im = Image.open(f) # open the image
    # convert to RGB bcs the file is in RGBA format, rotate 90 degree clockwise, resize image
    im = im.convert('RGB').rotate(-90).resize((128,128))
    file_basename = os.path.splitext(os.path.basename(f))[0]
    # save to /opt/icons directory
    im.save(os.path.join('/opt/icons/', file_basename + '.jpeg'))