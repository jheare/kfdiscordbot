import json

class WhatsMissing:

    def __init__(self):
        self.object_to_write = {}
        self.missing_json = "missingitems.json"
        self.final_json = "episodesmissingdata.json"

    def finish_up(self):
        with open(self.final_json, "w", encoding='utf-8') as final_json:
            json.dump(self.object_to_write, final_json, ensure_ascii=False)

    def create_object_to_write(self, episodenumber, episodetitle):
        # print(episode['title'])
        self.object_to_write[episodenumber] = {"Episode Title": episodetitle}

    # We're isolating every time 'Alex says' something
    def what_is_missing(self, episode):
        if len(episode['people']) < 1 and len(episode['themes']) < 1 and len(episode['notable_bits']) < 1:
            self.create_object_to_write(episode)
        # print(self.object_to_write)

    # Let's goooooooooooooooooooo
    def begin_refining(self):
        with open('final.json', encoding='utf-8') as raw_entities:
        # with open('finaltest.json', encoding='utf-8') as raw_entities:
            raw_entities_to_loop = json.load(raw_entities)
            # print("Hello")
            for episode in raw_entities_to_loop:
                if len(episode['people']) < 1 and len(episode['themes']) < 1 and len(episode['notable_bits']) < 1:
                    print(episode['title'])
                    self.create_object_to_write(episode['episode_number'], episode['title'])
                else:
                    continue
        self.finish_up()

findmissing = WhatsMissing()
findmissing.begin_refining()