import json
import re

from formatspecialepisodes import FormatSpecialEpisodes

formatspecial = FormatSpecialEpisodes()

# with open('searchresults.json', encoding='utf-8') as raw_entities:
#     tosearch = json.load(raw_entities)

class SortResults:

    def __init__(self):
        self.boop = "Boop"
        self.unsorted_episodes = {}
        self.sorted_episodes = {}
        self.finaljson = "searchresults.json"

    def finish_up(self):
        with open(self.finaljson, "w", encoding='utf-8') as finaljson:
            json.dump(self.sorted_episodes, finaljson, ensure_ascii=False)

    def if_sorted(self, key):
        if key in self.sorted_episodes:
            return True
        else:
            self.sorted_episodes[key] = {}
            return False

    def sort_keys_by_value(self):
        sorted_keys = sorted(self.unsorted_episodes)
        for item in sorted_keys:
            for k,v in self.unsorted_episodes[item].items():
                if k == "episode_title":
                    episode_name = v
                    self.if_sorted(episode_name)
                else:
                    self.sorted_episodes[episode_name][k] = v

    def if_exists_unsorted(self, key):
        if key in self.unsorted_episodes:
            return True
        else:
            return False

    def turn_to_int(self, episode_number):
        return (float(episode_number[0]))

###############################################################

# THIS IS THE HACKY-EST HACK THAT EVER HACKED BUT ALSO I'M DOING THIS FOR FUN
# ON AWS: - 
# I NEED TO RE-INDEX EVERYTHING AND RE-UPLOAD TO ELASTIC FILE SYSTEM FOR THIS NOT TO BE AN ISSUE
# ON DISCORD BOT: - 
# I ALSO NEED TO RE-INDEX BUT I'M ON A TRAIN AND NOT ENTIRELY SURE HOW TO DO SO BACK INTO LOCAL STORAGE
# DON'T WANT TO BE MESSING WITH THIS ON A SATURDAY BUT IF YOU'RE SEEING THIS - I AM AWARE
# THAT THIS IS DUMB AND I SHOULD DO BETTER

    def is_multipart_ep(self, episode_title):
        if "Obama Deception" in episode_title or "Endgame" in episode_title:
            return True

###############################################################

    def get_ep_number_and_title(self, episode_title):
        extract_episode_number = re.findall('.+?(?=: )', episode_title)
        if len(extract_episode_number) == 0:
            extract_episode_number = formatspecial.check_special_names(episode_title)
        if self.is_multipart_ep(episode_title):
            extract_episode_number = formatspecial.change_multipart_ep_description(episode_title)
        episode_number = self.turn_to_int(extract_episode_number)
        if self.if_exists_unsorted(episode_number) == False:
            self.unsorted_episodes[episode_number] = {}
            self.unsorted_episodes[episode_number]['episode_title'] = episode_title
        return episode_number

    def begin_sorting(self, results):
        print("Boop")
        for item in results:
            episode_number = self.get_ep_number_and_title(item)
            for k, v in results[item].items():
                self.unsorted_episodes[episode_number][k] = v
        self.sort_keys_by_value()
        self.finish_up()
        return self.sorted_episodes
        

# sortResults = SortResults()
# sortResults.begin_sorting(tosearch)