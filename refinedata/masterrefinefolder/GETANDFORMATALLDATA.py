import json
import datetime
import requests

from getbulkdata import GetBulkData
from getdeepdivedata import GetDeepDiveData
from formattingaliases import FormattingAliases
from combinedata import CombineData
from formatdataforsearch import FormatForSearch

class MasterFileGrabFormatData:

    def __init__(self):
        self.boop = "Boop"
        self.bulkdata = "final"
        self.deepdivedata = "raw_entities"
        self.date = ""

    def get_bulk_data(self):
        getting_bulk_data = GetBulkData()
        getting_bulk_data.begin_refining()

    def get_deep_dive_data(self):
        getting_deep_dive_data = GetDeepDiveData()
        getting_deep_dive_data.begin_refining()

    def format_aliases(self):
        formatting_aliases = FormattingAliases()
        formatting_aliases.begin_refining()

    def combine_data(self):
        combining_data = CombineData()
        combining_data.begin_refining()

    def formatting_for_search(self):
        format_for_discord = FormatForSearch()
        format_for_discord.begin_refining()

    def get_OG_files(self):
        self.date = str(datetime.date.today())
        bulkdatafilename = "./data/" + self.bulkdata + self.date + ".json"
        deepdivedatafilename = "./data/" + self.deepdivedata + self.date + ".json"
        bulkdata = requests.get('https://raw.githubusercontent.com/RainbowBatch/kfdb/master/final.json')
        deepdivedata = requests.get('https://raw.githubusercontent.com/RainbowBatch/kfdb/master/raw_entities.json')
        bulkdatastring = json.dumps(bulkdata.json())
        with open(bulkdatafilename, 'w') as f:
            f.write(bulkdatastring)
        f.close()
        deepdivedatastring = json.dumps(deepdivedata.json())
        with open(deepdivedatafilename, 'w') as f:
            f.write(deepdivedatastring)
        f.close()
        self.get_bulk_data()
        self.get_deep_dive_data()
        self.format_aliases()
        self.combine_data()
        self.formatting_for_search()

getall = MasterFileGrabFormatData()
getall.get_OG_files()