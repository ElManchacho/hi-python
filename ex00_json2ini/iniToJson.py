import configparser
import json

fichier = 'data.ini'

txt = {}

cfg = configparser.ConfigParser()

cfg.read(fichier)

sections = cfg.sections()

for section in sections :
	attrList = cfg[section].keys()
	sect = {}
	for attr in attrList :
		value = cfg.get(section,attr)
		sect[attr] = value
	txt[section] = sect

fichier_converti = open("dataEnd.json", "w")
json.dump(txt, fichier_converti, indent = 4)
fichier_converti.close()