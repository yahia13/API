import csv
import json
#This script is to convert the CSV file to Json
csvfilename = 'sheet1.csv'
jsonfilename = csvfilename.split('.')[0] + '.json'
csvfile = open(csvfilename, 'r')
jsonfile = open(jsonfilename, 'w')
reader = csv.DictReader(csvfile)
#defining the field names
fieldnames = ('title', 'description', 'image')
#Empty list to append
output = []
#Loop for each row of the CSV file
for each in reader:
  row = {}
  for field in fieldnames:
    row[field] = each[field]
  output.append(row)
#dumping to the json file after appending the list is complete
json.dump(output, jsonfile, indent=2, sort_keys=True)