import json


class CombineJSON:

    def __init__(self):
        self.object_to_write = {}
        self.main_data_dict = {}
        self.deep_dive_data_dict = {}
        # self.final_json = "combineddatatest.json"
        self.final_json = "combineddata.json"

    def finish_up(self):
        with open(self.final_json, "w", encoding='utf-8') as final_json:
            json.dump(self.main_data_dict, final_json, ensure_ascii=False)

    def combine_data(self):
        for large_episode_data in self.main_data_dict:
            print(large_episode_data)
            for deep_dive_data in self.deep_dive_data_dict:
                print(deep_dive_data)
                if deep_dive_data == large_episode_data:
                    self.main_data_dict[large_episode_data]['Deep Dive Topic'] = self.deep_dive_data_dict[deep_dive_data]['Deep Dive Topic']
                    self.main_data_dict[large_episode_data]['Aliases'] = self.deep_dive_data_dict[deep_dive_data]['Aliases']
        self.finish_up()


    def begin_refining(self):
        # with open('alexsaystest.json', encoding='utf-8') as raw_entities:
        with open('alexsays.json', encoding='utf-8') as raw_entities:
            self.main_data_dict = json.load(raw_entities)
        # with open('refinedaliasestest.json', encoding="utf-8") as raw_aliases:
        with open('refinedaliases.json', encoding="utf-8") as raw_aliases:
            self.deep_dive_data_dict = json.load(raw_aliases)
        self.combine_data()

        

combinedata = CombineJSON()
combinedata.begin_refining()