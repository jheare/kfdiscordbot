# GETTING deep_dive_topicS FROM KEYWORDS EXTRACTED FROM EPISODE TRANSCRIPTS
# ALSO ADDED aliases TO THESE SO THAT SEARCH WILL BE EASIER 

import json
import re
import datetime

class RefiningJSON():

    def __init__(self):
        self.object_to_write = {}
        self.finaljson = 'formattedsubjects'
        
    def finish_up(self):
        final_json_date = str(datetime.date.today())
        final_json_name = self.finaljson + final_json_date + ".json"
        with open(final_json_name, "w", encoding='utf-8') as finaljson:
            json.dump(self.object_to_write, finaljson, ensure_ascii=False)
                
    def make_objects(self, subject):
        for episodes in subject['grouped_entity_origin']:
            isolate_episode_string = re.match('\[\[(.*?): ', episodes)
            if isolate_episode_string == None:
                print("None")
            else:
                extract_episode_number = re.findall(r'\d+', isolate_episode_string.group(0))
                episode_number = ('').join(extract_episode_number)
                print(episode_number)
            # else:
            #     print(episodes)
                ################
                # episode_number = key[:3]
                if episode_number in self.object_to_write:
                    if subject["entity_name"] not in self.object_to_write[episode_number]['deep_dive_topics']:
                        self.object_to_write[episode_number]['deep_dive_topics'].append(subject["entity_name"])
                        self.object_to_write[episode_number]['aliases'].append(subject["entity_sourcetexts"])
                else:
                    self.object_to_write[episode_number] = {
                        "deep_dive_topics": [subject["entity_name"]], "aliases": [subject["entity_sourcetexts"]]}
                ###############
#        self.cleanup_values()

    def begin_refining(self):
        with open('raw_entities.json', encoding='utf-8') as raw_entities:
            raw_entities_to_loop = json.load(raw_entities)
            for item in raw_entities_to_loop:
                self.make_objects(item)
        self.finish_up()
                

refining = RefiningJSON()
refining.begin_refining()