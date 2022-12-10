
import json

# from sortresults import SortResults

# sortresults = SortResults()

class BeginRefiningSearch:

    def __init__(self):
        self.boop = "Boop"
        self.object_to_return = {}
        self.object_to_pass = {}
        self.queries = []
        self.finaljson = "searchresults.json"

#####################################

# This just exists so I can check my work in a json as opposed to in the console. Doesn't need to be here for non-debugging
# purposes

    def finish_up(self):
        with open(self.finaljson, "w", encoding='utf-8') as finaljson:
            json.dump(self.object_to_return, finaljson, ensure_ascii=False)

# This is removing duplicates from results

    def remove_duplicates(self, answer_array):
        # Rather than doing a for-loop I'm just converting it into a set and then back again
        toset = set(answer_array)
        return(list(toset))

# The search results from Whoosh don't care if they've found 4 episodes with two search queries so here we're checking to see if
# the episode is already in our object to return. 

    def if_exists(self, key):
        if key in self.object_to_return:
            return True
        else:
            self.object_to_return[key] = {}
            return False

# We _actually_ want to search through the pre-made arrays with information so here we're extracting the actual field we want to
# loop through. This is inefficient. I am a bb please be nice to me.

    def get_array_field_name(self, field):
        field_size = len(field)
        field_array_name = field[:field_size - 9]
        return field_array_name

# Looping through our arrays to see from whence this search result came and then returning said result/results

    def find_value(self, value):
        search_result = []
        for item in value:
            for q in self.queries:
                if q in item:
                    search_result.append(item)
        formatted_results = self.remove_duplicates(search_result)
        return formatted_results

    # So here we wanna do 4 things.
    # 1. Make a new object out of the episode title (use if_exists)
    # 2. Get the actual fields we wanna search (so topics_tostring becomes topics - use get_array_field_name)
    # 3. Find pass along the field we actually want to search so that we can return the search results (find_value)
    # 4. Add actual search results to the object to return

    def fill_out_names(self, itemtofilter):
        # print(itemtofilter['episode_title'])
        # if self.if_exists(itemtofilter['episode_title']):
        #     print("Yup")
        # else:
        #     self.object_to_return[itemtofilter['episode_title']] = {}
        for k, v in itemtofilter.items():
            if k == 'episode_title':
                continue
            if "b class=\"match term" in v:
                blank_field = self.get_array_field_name(k)
                to_add = self.find_value(itemtofilter[blank_field])
                if len(to_add) > 0:
                    self.if_exists(itemtofilter['episode_title'])
                    self.object_to_return[itemtofilter['episode_title']][blank_field] = to_add    

    # Just setting queries as an array in our class

    def set_query(self, queries):
        if type(queries) == list:
            self.queries = queries
        else:
            self.queries = queries.split()

    # So first things first we're going to set the queries to a list (because if you just have a single query and we're filtering instead of searching you're gonna need it

    # Then we're gonna put the search results into an object so we can manipulate said object. Then we're gonna iterate!

    def begin_refining(self, search_results, queries):
        self.set_query(queries)
        self.object_to_pass = search_results
        for item in self.object_to_pass:
            self.fill_out_names(item)
        return self.object_to_return
        
        # self.finish_up()
