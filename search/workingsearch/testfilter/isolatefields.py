import re

import json

# with open('object_to_iterate.json', encoding='utf-8') as raw_entities:
#     tosearch = json.load(raw_entities)

class addAdditionalFields():

    def __init__(self):
        self.boop = "Boop"
        self.object_to_filter = {}
        self.object_to_pass = {}
        self.finaljson = "secondaryobject.json"

    def finish_up(self):
        with open(self.finaljson, "w", encoding='utf-8') as finaljson:
            json.dump(self.object_to_pass, finaljson, ensure_ascii=False)

    def get_array_field_name(self, field):
        field_size = len(field)
        field_array_name = field[:field_size - 9]
        return field_array_name

    def if_exists(self, key):
        if key in self.object_to_pass:
            return True
        else:
            return False

    def fill_out_names(self, itemtofilter):
        print(itemtofilter['episode_title'])
        if self.if_exists(itemtofilter['episode_title']):
            print("Yup")
        else:
            self.object_to_pass[itemtofilter['episode_title']] = {}
        for k, v in itemtofilter.items():
            if k == 'episode_title':
                continue
            else:
                if v != []:
                    new_key_to_add = self.get_array_field_name(k)
                    self.object_to_pass[itemtofilter['episode_title']][new_key_to_add] = []
                self.object_to_pass[itemtofilter['episode_title']][k] = v

    def set_object_to_filter(self, object):
        self.object_to_filter = object
        for item in self.object_to_filter:
            self.fill_out_names(self.object_to_filter[item])
            # print(item)
        # print(self.object_to_pass)
        self.finish_up()
        return self.object_to_pass


# filter = addAdditionalFields()
# filter.set_object_to_filter()
