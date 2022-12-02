import json

from refiningresults import RefiningResults

class BeginRefiningSearch:

    def __init__(self):
        self.boop = "Boop"
        self.object_to_return = {}
        self.object_to_pass = {}
        self.final_object_with_arrays = {}

# Let's get the good stuff bb (by which I mean lets get the arrays which contain the data we want)

    def assign_arrays_to_key(self, field, individual_results):
        for entries in individual_results:
            if field in entries:
                self.final_object_with_arrays[field] = individual_results[field]
                
        return self.final_object_with_arrays

    def extract_entry_data(self, field, search_results):
        for individual_results in search_results:
            self.assign_arrays_to_key(field, individual_results)

    def get_arrays(self, array_field_names, search_results):
        print(search_results[0]['episode_title'])
        self.final_object_with_arrays['episode_title'] = search_results[0]['episode_title']
        print(self.final_object_with_arrays)
        print("This is before our second for loop")
        for field in array_field_names:
            self.extract_entry_data(field, search_results)

# Getting the names of the fields I **actually** want to search through in the end
# What a faff

    def get_array_field_name(self, field):
        field_size = len(field)
        field_array_name = field[:field_size - 9]
        return field_array_name

    def getting_field_arrays(self, new_object_entry):
        fields_to_get = []
        for values in new_object_entry:
            field_array_name = self.get_array_field_name(values)
            fields_to_get.append(field_array_name)
        print(fields_to_get)
        return fields_to_get

# I'm just unifying the results into one object in case I need them. This is probably redundant

    def unifying_object(self, new_object_entry):
        for value in new_object_entry:
            self.object_to_pass[value] = new_object_entry[value]


# In this section I am just looping over the results to filter out the data which matches the query
# So:
# Begin refining - has the entire object returned during search
# Loop through all results - extracts which fields contain a match with the original search term and then pass only those fields along


    def loop_through_search_results(self, returned_items, count):
        for k, v in returned_items.items():
            if "b class=\"match term" in v:
                self.object_to_pass[count][k] = v
            else:
                continue
        

    def begin_refining(self, fields, search_results, query):
        self.final_object_with_arrays = {}
        count = 0
        for i in search_results:
            self.object_to_pass[count] = {}
            self.object_to_pass[count]['episode_title'] = search_results[count]['episode_title']
            self.loop_through_search_results(i, count)
            count += 1
        print(self.object_to_pass)
        print("Boooooop")
        # print(self.final_object_with_arrays)
