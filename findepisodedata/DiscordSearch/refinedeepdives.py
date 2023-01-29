import json
import re

class BeginRefiningSearch:

    def __init__(self):
        self.boop = "Boop"
        self.object_to_return = {}
        self.sorted_object_to_return = {}
        self.object_to_pass = {}
        self.final_array_to_return = []
        self.finaljson = "searchresults.json"

#####################################

# This just exists so I can check my work in a json as opposed to in the console. Doesn't need to be here for non-debugging
# purposes

    def finish_up(self):
        with open(self.finaljson, "w", encoding='utf-8') as finaljson:
            json.dump(self.final_array_to_return, finaljson, ensure_ascii=False)

# Append the episode names to an array to return (no need for an object on this one!)

    def append_episode_to_array(self, episode):
        self.final_array_to_return.append(episode)

# Sort the object to return so that episodes are returned in order

    def sort_keys_by_value(self):
        for key in sorted(self.object_to_return):
            self.sorted_object_to_return[key] = self.object_to_return[key]
            self.append_episode_to_array(self.object_to_return[key]['episode_title'])

# The search results from Whoosh don't care if they've found 4 episodes with two search queries so here we're checking to see if
# the episode is already in our object to return. 

    def if_exists(self, key):
        if key in self.object_to_return:
            return True
        else:
            return False

    # Here I'm separating the episode number from the episode title to make a sortable object

    def turn_to_int(self, episode_number):
        return (int(episode_number[0]))

    def get_ep_number_and_title(self, episode_title):
        extract_episode_number = re.findall('.+?(?=: )', episode_title)
        episode_number = self.turn_to_int(extract_episode_number)
        if self.if_exists(episode_number) == False:
            self.object_to_return[episode_number] = {}
            self.object_to_return[episode_number]['episode_title'] = episode_title

    # So first things first we're going to set the queries to a list (because if you just have a single query and we're filtering 
    # instead of searching you're gonna need it

    # Then we're gonna put the search results into an object so we can manipulate said object. Then we're gonna iterate!

    def begin_refining(self, search_results):
        self.object_to_pass = search_results
        for item in self.object_to_pass:
            # self.extract_episodes(item)
            self.get_ep_number_and_title(item['episode_title'])
        self.sort_keys_by_value()
        self.finish_up()
