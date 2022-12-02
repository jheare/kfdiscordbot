import json

class RefiningResults:

    def __init__(self):
        self.boop = "Boop"
        self.results = {}
        self.count = 1

    def add_results(self, final_results):
        self.results[self.count] = final_results
        self.count += 1
        print(self.results)
        print("Here lies results")

    def getResults(self, query, final_results):
        # print(final_results)
        # print("HEY THESE ARE MY RESULTS UP HERE! ^^^^")
        # print(query)
        # print("MY QUERY IS UP HERE BB")
        self.add_results(final_results)
        

