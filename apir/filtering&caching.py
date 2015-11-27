from __future__ import print_function
import json
from PIL import Image
import urllib.request

#This script is for filtering the bas urls, then saving the images at static directory then updating the json file
output = []

with open('sheet1.json') as json_data:
    data = json.load(json_data)
    for row in data:
        #checks if the image url is empty
        if (row['image'] == ''):
            pass
        else:
            try:
                #opens the link to check if it is an image
                with urllib.request.urlopen(row['image']) as response:
                    try:
                        #now it is definite that it is an image
                        #set max size of the image then saving it after.
                        maxsize = (768,768)
                        name = 'static/apir/' + row['description'] + '.jpg'
                        jsname = 'apir/' + row['description'] + '.jpg'
                        im = Image.open(response)
                        im.thumbnail(maxsize)
                        im.save(name)
                        row ['image'] = '%s' %(jsname)
                        output.append(row)
                    except ValueError:
                        pass
            except IOError:
                pass
#updating the json file
with open('sheet1.json', 'w') as json_data:
    json.dump(output,json_data,indent = 2)