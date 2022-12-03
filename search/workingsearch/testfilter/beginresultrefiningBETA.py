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
        self.final_object_with_arrays = {}
        self.finaljson = "objecttoiterate.json"

#####################################

    def finish_up(self):
        with open(self.finaljson, "w", encoding='utf-8') as finaljson:
            json.dump(self.object_to_pass, finaljson, ensure_ascii=False)

# Here is where I add the fields that we're actually going to be searching through for the key phrases
# Note that I'm forcing the dictionary object (object_to_pass[count]) into a list

# In this section I am just looping over the results to filter out the data which matches the query
# So:
# Begin refining - has the entire object returned during search
# Loop through all results - extracts which fields contain a match with the original search term and then pass only those fields along
# After that and the above are done we pass it over to the Isolate Search class to whittle it down

    def get_array_field_name(self, field):
        field_size = len(field)
        field_array_name = field[:field_size - 9]
        return field_array_name

    def loop_through_search_results(self, returned_items, count):
        for k, v in returned_items.items():
            if "b class=\"match term" in v:
                blank_field = self.get_array_field_name(k)
                self.object_to_pass[count][blank_field] = []
                self.object_to_pass[count][k] = v
            else:
                continue

    def begin_refining(self, search_results, queries):
        self.final_object_with_arrays = {}
        self.object_to_pass = {}
        count = 0
        if type(queries) == list:
            for i in search_results:
                self.object_to_pass[count] = {}
                self.object_to_pass[count]['episode_title'] = search_results[count]['episode_title']
                self.loop_through_search_results(i, count)
                count += 1
        else:
            # print("BOOP")
            self.object_to_pass[count] = {}
            self.object_to_pass[count]['episode_title'] = search_results[0]['episode_title']
            self.loop_through_search_results(search_results[0], count)
        empty_fields = add_fields.set_object_to_filter(self.object_to_pass, search_results, queries)
        # final_results.set_objects(search_results, empty_fields, queries)
        self.finish_up()
        # print(self.object_to_pass)
        # print("FINAL OBJECT TO PASS")
        
