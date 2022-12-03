import re

import json

with open('object_to_iterate.json', encoding='utf-8') as raw_entities:
    tosearch = json.load(raw_entities)

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
                    print(new_key_to_add)
                    print(v)
                    print("This should be the value that doesn't have anything in it")
                    self.object_to_pass[itemtofilter['episode_title']][new_key_to_add] = []
                self.object_to_pass[itemtofilter['episode_title']][k] = v
                # else:
                #     print(k)
                #     print(v)
                #     print("And this should be the value with nothing in it?")
                #     self.object_to_pass[itemtofilter['episode_title']][k] = v

    def set_object_to_filter(self):
        self.object_to_filter = tosearch
        for item in self.object_to_filter:
            self.fill_out_names(self.object_to_filter[item])
            # print(item)
        # print(self.object_to_pass)
        self.finish_up()


filter = addAdditionalFields()
filter.set_object_to_filter()

# str_search = re.findall(r'\/b>$', string_to_search)
# print(str_search)

# arr = string_to_search.split()
# print(arr)

# for word in arr:
#     if word.endswith('</b>'):
#         # print(word)
#         word_size = len(word)
#         new_word = word[:7 - word_size]
#         print(new_word)
#     # else:
#         # print(word)
#         # continue
    


# ### None of these do what I want and that is entirely my fault but I don't know why

# # result = re.search('<b class=\"match term(.*)</b>', string_to_search)
# # print(result.group(1))
# # print("This is our normal search result")

# # list = re.findall('[<b class="match term]\w+', string_to_search)
# # print(list)
# # print("This is the list")
# # replaced = re.sub(' ', '', string_to_search)
# # print(replaced)
# # result2 = re.search('<b class="match term0(.*)</b>', replaced)
# # print(result2)
# # print("This is the result when it's all squished up")
# # # print(result2)
# # print(re.findall('<b class="match term(.*)</b>', string_to_search))
# # print("This is evething apparently")

# # text = "I was searching my source to make a big desk yesterday."
# # text_to_find = '<b class="match term'

# # boop = re.findall(r'\b"<b class=\"match term"\w+', string_to_search)
# # print(boop)
# print(re.search(r'\/b>$', string_to_search))

# boop = re.match(pattern='\</b>$', string=string_to_search)
# print(boop)