import json
import csv

with open('baseJson.json') as fichier_json:
    data = json.load(fichier_json)
 
eleves = data['eleves']

toCsv = open('ficher_converti.csv', 'w')

csv_writer = csv.writer(toCsv)

count = 0
 
for el in eleves:
    if count == 0:

        header = el.keys()
        csv_writer.writerow(header)
        count += 1
        
    csv_writer.writerow(el.values())
 
toCsv.close()