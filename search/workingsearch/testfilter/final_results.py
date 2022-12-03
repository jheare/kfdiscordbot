import json

class finalResults:

    def __init__(self):
        self.boop = "Boop"
        self.full_search_results = {}
        self.fields_to_search = {}
        self.final_object = {}
        self.queries = []
        self.finaljson = "finaljson.json"

    def set_objects(self, full_search_results, empty_fields, queries):
        self.full_search_results = full_search_results
        self.fields_to_search = empty_fields
        self.queries = queries
        print(queries)
        print(len(self.full_search_results))
        print(len(self.fields_to_search))