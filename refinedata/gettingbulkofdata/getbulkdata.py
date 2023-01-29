# THIS CLASS IS CALLED ALEXSAYS BECAUSE I WAS ORIGINALLY JUST TRYING TO EXTRACT ALL THE INSTANCES OF THE RAW
# DATA WHERE IT BEGINS WITH 'ALEX SAYS' BUT IT EXPANDED INTO
# * 'ALEX SAYS'
# * PEOPLE
# * TOPICS

import json

class AlexSays:

    def __init__(self):
        self.object_to_write = {}
        self.alex_says_array = []
        self.topics_array = []
        # self.final_json = "alexsaystest.json"
        self.final_json = "alexsaysupdated.json"

    def finish_up(self):
        with open(self.final_json, "w", encoding='utf-8') as final_json:
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
        self.object_to_write[episodenumber] = {"Episode Title": episodetitle, "Alex says": self.alex_says_array, "Topics": self.topics_array, "People": peopleinepisode}

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
        with open('finalupdated.json', encoding='utf-8') as raw_entities:
        # with open('finaltest.json', encoding='utf-8') as raw_entities:
            raw_entities_to_loop = json.load(raw_entities)
            for episodes in raw_entities_to_loop:
                self.get_the_says(episodes)
        self.finish_up()


getalexsays = AlexSays()
getalexsays.begin_refining()

