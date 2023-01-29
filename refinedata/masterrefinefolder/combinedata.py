import json
import datetime

class CombineData:

    def __init__(self):
        self.object_to_write = {}
        self.main_data_dict = {}
        self.deep_dive_data_dict = {}
        self.final_json = "combineddata"
        self.date = ""

    def finish_up(self):
        final_json_name = "./data/" + self.final_json + self.date + ".json"
        with open(final_json_name, "w", encoding='utf-8') as final_json:
            json.dump(self.main_data_dict, final_json, ensure_ascii=False)

    def combine_data(self):
        for large_episode_data in self.main_data_dict:
            # print(large_episode_data)
            for deep_dive_data in self.deep_dive_data_dict:
                # print(deep_dive_data)
                if deep_dive_data == large_episode_data:
                    self.main_data_dict[large_episode_data]['deep_dive_topics'] = self.deep_dive_data_dict[deep_dive_data]['deep_dive_topics']
                    self.main_data_dict[large_episode_data]['aliases'] = self.deep_dive_data_dict[deep_dive_data]['aliases']
        self.finish_up()


    def begin_refining(self):
        self.date = str(datetime.date.today())
        bulkdata = "./data/bulkdata" + self.date + ".json"
        deepdivesubjectdata = "./data/formattedaliases" + self.date + ".json"
        with open(bulkdata, encoding='utf-8') as raw_entities:
            self.main_data_dict = json.load(raw_entities)
        with open(deepdivesubjectdata, encoding="utf-8") as raw_aliases:
            self.deep_dive_data_dict = json.load(raw_aliases)
        self.combine_data()

        

# combinedata = CombineData()
# combinedata.begin_refining()