import json
import os
import whoosh
import os.path
from whoosh.fields import *
from whoosh.analysis import StemmingAnalyzer

from typing import Dict, List, Sequence

from workingsearchforlambda import SearchEngine
from beginresultrefining import BeginRefiningSearch
from sortresults import SortResults

schema = Schema(
    episode_title=ID(stored=True),
    topics_tostring=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    topics=KEYWORD(stored=True),
    people_tostring=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    people=KEYWORD(stored=True),
    alex_says_tostring=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    alex_says=KEYWORD(stored=True),
    deep_dive_topic_tostring=TEXT(
        stored=True, analyzer=StemmingAnalyzer()),
    deep_dive_topic=KEYWORD(stored=True),
    deep_dive_aliases_tostring=TEXT(
        stored=True, analyzer=StemmingAnalyzer())
)

engine = SearchEngine(schema)
refining = BeginRefiningSearch()
sorting = SortResults()


class StartEngine:

    def __init__(self):
        self.boop = "Boop"


    def run_filtered_query(self, field, query):
        topic_to_search = ('').join(field)
        for q in query:
            engine.filtering(topic_to_search, q, highlight=True)
        refining.begin_refining(engine.results_to_refine, engine.queries)
        sorting.begin_sorting(refining.object_to_return)

    def run_multi_query(self, fields, query):
        for q in query:
            engine.query(q, fields, highlight=True)
        refining.begin_refining(engine.results_to_refine, engine.queries)
        sorting.begin_sorting(refining.object_to_return)

    def start_engine(self, fields, query):
        print(len(fields))
        if len(fields) == 1:
            self.run_filtered_query(fields, query)
        if len(fields) > 1:
            self.run_multi_query(fields, query)

searching = StartEngine()
searching.start_engine(["topics_tostring", "alex_says_tostring", "people_tostring"], ["shit", "fuck"])
