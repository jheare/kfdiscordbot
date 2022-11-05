# GETTING DEEP DIVE TOPICS FROM KEYWORDS EXTRACTED FROM EPISODE TRANSCRIPTS
# ALSO ADDED ALIASES TO THESE SO THAT SEARCH WILL BE EASIER 

import json
import re

class RefiningJSON():

    def __init__(self):
        self.object_to_write = {}
        # self.finaljson = 'formattedsubjectstesting.json'
        self.finaljson = 'formattedsubjects.json'
        
    def finish_up(self):
        with open(self.finaljson, "w", encoding='utf-8') as finaljson:
            json.dump(self.object_to_write, finaljson, ensure_ascii=False)

    def cleanup_values(self):
        self.finish_up()
                

    def make_objects(self, subject):
        for key, value in subject['entity_origin'].items():
            relevant_key = 'transcript'
            if relevant_key in key:
                numbers = re.findall(r'\d+', key)
                numbers_to_str = ''.join(numbers)
                if numbers_to_str in self.object_to_write:
                    if subject["entity_name"] not in self.object_to_write[numbers_to_str]['Deep Dive Topic']:
                        self.object_to_write[numbers_to_str]['Deep Dive Topic'].append(subject["entity_name"])
                        self.object_to_write[numbers_to_str]['Aliases'].append(subject["entity_sourcetexts"])
                else:
                    self.object_to_write[numbers_to_str] = {
                        "Deep Dive Topic": [subject["entity_name"]], "Aliases": [subject["entity_sourcetexts"]]}
        self.cleanup_values()

    def begin_refining(self):
        with open('raw_entities.json', encoding='utf-8') as raw_entities:
        # with open('raw_entities_test.json', encoding='utf-8') as raw_entities:
            raw_entities_to_loop = json.load(raw_entities)
            for item in raw_entities_to_loop:
                self.make_objects(item)
                





refining = RefiningJSON()
refining.begin_refining()