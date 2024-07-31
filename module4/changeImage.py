#!/usr/bin/env python3

import os
from PIL import Image

directory = 'supplier-data/images/'

for file in os.listdir(directory):
  if '.DS_Store' not in file and file.endswith('.tiff'):
    f = os.path.join(directory, file)
    im = Image.open(f)
    im = im.convert('RGB').resize((600,400))
    file_basename = os.path.splitext(os.path.basename(f))[0]
    im.save(os.path.join(directory, file_basename + '.jpeg'))