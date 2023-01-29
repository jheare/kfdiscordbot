import json
import datetime
import re

class NewDataFormat:

    def __init__(self):
        self.boop = "Boop"
        self.object_to_write = {}
        self.final_json = "data_formatted_for_search"
        self.date = ""

    def finish_up(self):
        final_json_filename = self.final_json + self.date + ".json"
        with open(final_json_filename, "w", encoding='utf-8') as final_json:
            json.dump(self.object_to_write, final_json, ensure_ascii=False)

    def reformatting_data(self, raw_entities_to_loop, episodenumber):
        # print(episodenumber)
        self.object_to_write[episodenumber] = {}
        for episode_data in raw_entities_to_loop:
            # print(episode)
            if episode_data == 'episode_title':
                self.object_to_write[episodenumber][episode_data] = raw_entities_to_loop[episode_data]
            else:
                to_string = episode_data + "_tostring"
                print(to_string)
                if type(raw_entities_to_loop[episode_data]) == str:
                    string_to_add = raw_entities_to_loop[episode_data]
                else:
                    string_to_add = (' ').join(raw_entities_to_loop[episode_data])
                self.object_to_write[episodenumber][to_string] = string_to_add
                self.object_to_write[episodenumber][episode_data] = raw_entities_to_loop[episode_data]
        # print(self.object_to_write)
        ####
        # print(self.object_to_write)


    def begin_refining(self):
        self.date = str(datetime.date.today())
        to_open_filename = "combineddata" + self.date + ".json"
        with open(to_open_filename, encoding='utf-8') as raw_entities:
            raw_entities_to_loop = json.load(raw_entities)
            for item in raw_entities_to_loop:
                # print(raw_entities_to_loop[item])
                self.reformatting_data(raw_entities_to_loop[item], item)
                # break
        # print(self.object_to_write)
        self.finish_up()

new_data_format = NewDataFormat()
new_data_format.begin_refining()