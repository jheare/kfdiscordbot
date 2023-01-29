import json
import datetime
import re

class NewDataFormat:

    def __init__(self):
        self.boop = "Boop"
        self.object_to_write = {}
        self.final_json = "reformatted_data.json"

    def finish_up(self):
        with open(self.final_json, "w", encoding='utf-8') as final_json:
            json.dump(self.object_to_write, final_json, ensure_ascii=False)

    def reformatting_data(self, raw_entities_to_loop, episodenumber):
        # print(episodenumber)
        self.object_to_write[episodenumber] = {}
        for episode_data in raw_entities_to_loop:
            lowercase_data = episode_data.lower()
            print(lowercase_data)
            if lowercase_data == 'episode_title':
                print(lowercase_data)
                self.object_to_write[episodenumber][lowercase_data] = raw_entities_to_loop[lowercase_data]
            else:
                to_string = lowercase_data + "_tostring"
                print(to_string)
                # if type(raw_entities_to_loop[episode_data]) == str:
                #     string_to_add = raw_entities_to_loop[episode_data]
                # else:
                #     string_to_add = (' ').join(raw_entities_to_loop[episode_data])
                # self.object_to_write[episodenumber][to_string] = string_to_add
                # self.object_to_write[episodenumber][episode_data] = raw_entities_to_loop[episode_data]
            ####
            # if episode_data.lower() == 'episode_title':
            #     self.object_to_write[episodenumber][episode_data] = raw_entities_to_loop[episode_data]
            # else:
            #     to_string = episode_data + "_tostring"
            #     print(to_string)
            #     if type(raw_entities_to_loop[episode_data]) == str:
            #         string_to_add = raw_entities_to_loop[episode_data]
            #     else:
            #         string_to_add = (' ').join(raw_entities_to_loop[episode_data])
            #     self.object_to_write[episodenumber][to_string] = string_to_add
            #     self.object_to_write[episodenumber][episode_data] = raw_entities_to_loop[episode_data]
        ####
        # print(self.object_to_write)


    def begin_refining(self):
        # with open('subjectstoformattest.json', encoding='utf-8') as raw_entities:
        with open('combineddataupdated.json', encoding='utf-8') as raw_entities:
            raw_entities_to_loop = json.load(raw_entities)
            for item in raw_entities_to_loop:
                # print(raw_entities_to_loop[item])
                self.reformatting_data(raw_entities_to_loop[item], item)
                # break
        print(self.object_to_write)
        # self.finish_up()

new_data_format = NewDataFormat()
new_data_format.begin_refining()