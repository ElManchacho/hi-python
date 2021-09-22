import json

fichier = 'data.txt'

dict1 = {}

with open(fichier) as file:

	for line in file:

		attr, value = line.strip().split(None, 1)

		dict1[attr] = value.strip()

fichier_converti = open("fichier_converti.json", "w")
json.dump(dict1, fichier_converti, indent = 4)
fichier_converti.close()
