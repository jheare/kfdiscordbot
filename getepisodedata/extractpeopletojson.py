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
    with open(jsonname, "w", encoding="utf-8") as outfile:
        json.dump(dicttowritetojson, outfile, ensure_ascii=False)

episodecsvtojson(r'ExportedEpisodeDetails.csv')