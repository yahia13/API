import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import csv

#this was an attempt to use Google's developer tools to use DRIVE API. It was intended to call the CSV
#file instead of saving it locally
json_key = json.load(open('MyProject-53cd8085b842.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

sht1 = gc.open_by_key('19CtR3Wuszozzpj2hj4lmcYpMPK9_c2Y9FQQsFigggeU')



jsonfilename = sht1.split('.')[0] + '.json'
csvfile = open(sht1, 'r')
jsonfile = open(jsonfilename, 'w')
reader = csv.DictReader(csvfile)

fieldnames = ('title', 'description', 'image')

output = []

for each in reader:
  row = {}
  for field in fieldnames:
    row[field] = each[field]
  output.append(row)

json.dump(output, jsonfile, indent=2, sort_keys=True)