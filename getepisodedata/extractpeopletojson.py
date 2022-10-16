import csv
import json
import datetime

def episodecsvtojson(csvfile):
    dicttowritetojson = {}
    jsonname = "KFEpisodeData" + str(datetime.date.today()) + ".json"
    with open(csvfile, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            if len(rows['people']) > 2:
                key = rows['episode_number']
                dicttowritetojson[key] = rows['people'].lower()
    with open(jsonname, "w") as outfile:
        json.dump(dicttowritetojson, outfile)

episodecsvtojson(r'ExportedEpisodeDetails.csv')