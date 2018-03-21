#!/usr/bin/env python3
'''
reads in train.csv, prints the shape and head
uses requests library to download the first 10 images
add comments to lines 39 & 40 to run full script
script tests to see if image exists
'''
import pandas as pd
import sys, requests, shutil, os

data_dir = "../landmark_data/"
data_in = "train.csv"
df = pd.read_csv(os.path.join(data_dir, data_in))
print("Shape: {}\n".format(df.shape))
print(df.head())

data_out = os.path.join(data_dir, "train_images/")
if not os.path.exists(data_out):
    os.mkdir(data_out)

def get_image(path):
    response = requests.get(path, stream=True)
    with open(os.path.join(data_out, 'image.jpg'), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

links = df.url
i = 0

for link in links:
    if os.path.exists(os.path.join(data_out, str(i)+'.jpg')):
        i += 1
        continue
    get_image(link)
    new_file = os.path.join(data_out, 'image.jpg')
    new_file_name = os.path.join(data_out, str(i)+'.jpg')
    os.rename(new_file, new_file_name)
    i += 1
    if i == 10:
        break
