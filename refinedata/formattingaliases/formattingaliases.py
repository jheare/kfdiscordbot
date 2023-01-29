import json
import datetime
import re


class SortOutAliases():

    def __init__(self):
        self.object_to_write = {}
        # self.final_json = "refiningaliasestest.json"
        self.final_json = "refinedaliasesupdated.json"

    def finish_up(self):
        with open(self.final_json, "w", encoding='utf-8') as final_json:
            json.dump(self.object_to_write, final_json, ensure_ascii=False)

    def refinealiases(self, episodedetails, episodenumber):
        array_of_aliases = []
        new_key = episodenumber
        for key, value in episodedetails.items():
            if key == "Aliases":
                aliases_to_loop = value
                for list_of_aliases_to_loop in aliases_to_loop:
                    for key, value in list_of_aliases_to_loop.items():
                        if "\n" not in key:
                            array_of_aliases.append(key)
        episodedetails['Aliases'] = array_of_aliases
        self.object_to_write[new_key] = {
            "Deep Dive Topic": episodedetails['Deep Dive Topic'], "Aliases": episodedetails['Aliases']
        }


    def begin_refining(self):
        # with open('subjectstoformattest.json', encoding='utf-8') as raw_entities:
        with open('formattedsubjectsupdated.json', encoding='utf-8') as raw_entities:
            raw_entities_to_loop = json.load(raw_entities)
            for item in raw_entities_to_loop:
                print(item)
                self.refinealiases(raw_entities_to_loop[item], item)
                # break
        self.finish_up()

refine = SortOutAliases()
refine.begin_refining()