from isolateactualsearch import IsolateResults
from isolatefields import addAdditionalFields
from final_results import finalResults
import json

isolatingresults = IsolateResults()
add_fields = addAdditionalFields()
final_results = finalResults()

class BeginRefiningSearch:

    def __init__(self):
        self.boop = "Boop"
        self.object_to_return = {}
        self.object_to_pass = {}
        self.queries = []
        self.finaljson = "objecttoiterate.json"

#####################################

    def finish_up(self):
        with open(self.finaljson, "w", encoding='utf-8') as finaljson:
            json.dump(self.object_to_return, finaljson, ensure_ascii=False)

# Here is where I add the fields that we're actually going to be searching through for the key phrases
# Note that I'm forcing the dictionary object (object_to_pass[count]) into a list

# In this section I am just looping over the results to filter out the data which matches the query
# So:
# Begin refining - has the entire object returned during search
# Loop through all results - extracts which fields contain a match with the original search term and then pass only those fields along
# After that and the above are done we pass it over to the Isolate Search class to whittle it down

    def if_exists(self, key):
        if key in self.object_to_return:
            return True
        else:
            return False

    def get_array_field_name(self, field):
        field_size = len(field)
        field_array_name = field[:field_size - 9]
        return field_array_name

    def find_value(self, value):
        search_result = []
        for item in value:
            for q in self.queries:
                if q in item:
                    search_result.append(item)
        return search_result

    def fill_out_names(self, itemtofilter):
        print(itemtofilter['episode_title'])
        if self.if_exists(itemtofilter['episode_title']):
            print("Yup")
        else:
            self.object_to_return[itemtofilter['episode_title']] = {}
        for k, v in itemtofilter.items():
            if k == 'episode_title':
                continue
            if "b class=\"match term" in v:
                blank_field = self.get_array_field_name(k)
                to_add = self.find_value(itemtofilter[blank_field])
                if len(to_add) > 0:
                    self.object_to_return[itemtofilter['episode_title']][blank_field] = to_add    

    def begin_refining(self, search_results, queries):
        self.queries = queries
        self.object_to_pass = search_results
        for item in self.object_to_pass:
            self.fill_out_names(item)
        self.finish_up()
