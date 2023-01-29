import json
import datetime
import re


class FormattingAliases():

    def __init__(self):
        self.object_to_write = {}
        self.final_json = "formattedaliases"
        self.date = ""

    def finish_up(self):
        final_json_name = "./data/" + self.final_json + self.date + ".json"
        with open(final_json_name, "w", encoding='utf-8') as final_json:
            json.dump(self.object_to_write, final_json, ensure_ascii=False)

    def refinealiases(self, episodedetails, episodenumber):
        array_of_aliases = []
        new_key = episodenumber
        for key, value in episodedetails.items():
            if key == "aliases":
                aliases_to_loop = value
                for list_of_aliases_to_loop in aliases_to_loop:
                    for key, value in list_of_aliases_to_loop.items():
                        if "\n" not in key:
                            array_of_aliases.append(key)
        episodedetails['aliases'] = array_of_aliases
        self.object_to_write[new_key] = {
            "deep_dive_topics": episodedetails['deep_dive_topics'], "aliases": episodedetails['aliases']
        }

    def begin_refining(self):
        # with open('subjectstoformattest.json', encoding='utf-8') as raw_entities:
        self.date = str(datetime.date.today())
        json_to_open_name = "./data/deepdivedata" + self.date + ".json"
        with open(json_to_open_name, encoding='utf-8') as raw_entities:
            raw_entities_to_loop = json.load(raw_entities)
            for item in raw_entities_to_loop:
                self.refinealiases(raw_entities_to_loop[item], item)
        self.finish_up()

# refine = FormattingAliases()
# refine.begin_refining()