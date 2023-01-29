# THIS CLASS IS CALLED ALEXSAYS BECAUSE I WAS ORIGINALLY JUST TRYING TO EXTRACT ALL THE INSTANCES OF THE RAW
# DATA WHERE IT BEGINS WITH 'ALEX SAYS' BUT IT EXPANDED INTO
# * 'ALEX SAYS'
# * PEOPLE
# * TOPICS

import json
import datetime

class GetBulkData:

    def __init__(self):
        self.object_to_write = {}
        self.alex_says_array = []
        self.topics_array = []
        self.final_json = "bulkdata"
        self.date = ""

    def finish_up(self):
        final_json_file_name = "./data/" + self.final_json + self.date + ".json"
        with open(final_json_file_name, "w", encoding='utf-8') as final_json:
            json.dump(self.object_to_write, final_json, ensure_ascii=False)

    # If this doesn't count as something alex said, it goes in topics instead
    def get_topics(self, topics):
        # print(topics)
        self.topics_array.append(topics)

    # This removes the 'Alex Says' portion of the string and just returns
    # an array containing _what_ Alex said
    def remove_alex_says_string(self, string):
        if 'Alex says ' in string:
            self.alex_says_array.append(string[10:])
        else:
            self.get_topics(string)

    # We're creating the object we're going to write into a json file
    def creating_object_to_write(self, episodenumber, episodetitle, peopleinepisode):
        self.object_to_write[episodenumber] = {"episode_title": episodetitle, "alex_says": self.alex_says_array, "topics": self.topics_array, "people": peopleinepisode}

    # We're isolating every time 'Alex says' something
    def get_the_says(self, episode):
        self.alex_says_array = []
        self.topics_array = []
        for items in episode['notable_bits']:
            self.remove_alex_says_string(items)
        for items in episode['themes']:
            self.remove_alex_says_string(items)
        self.creating_object_to_write(episode['episode_number'], episode['title'], episode['people'])

    # Let's goooooooooooooooooooo
    def begin_refining(self):
        self.date = str(datetime.date.today())
        bulkdatafilename = "./data/final" + self.date + ".json"
        with open(bulkdatafilename, encoding='utf-8') as raw_entities:
        # with open('finaltest.json', encoding='utf-8') as raw_entities:
            raw_entities_to_loop = json.load(raw_entities)
            for episodes in raw_entities_to_loop:
                self.get_the_says(episodes)
        self.finish_up()

# getbulkdata = GetBulkData()
# getbulkdata.begin_refining()

