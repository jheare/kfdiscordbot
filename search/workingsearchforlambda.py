import json
import whoosh
from typing import Dict, List, Sequence

import os.path

from beginresultrefining import BeginRefiningSearch

from whoosh.index import create_in, exists_in, open_dir
from whoosh.fields import *
from whoosh.qparser import MultifieldParser
from whoosh.filedb.filestore import RamStorage
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import QueryParser

from whoosh import query
from whoosh.query import Term


##########################
# OG REPO NOTES

# I TOOK THE BASIC TEMPLATE FOR THIS FROM THIS GITHUB REPO - https://github.com/darenr/python-whoosh-simple-example/blob/master/example.py
# I HAVE ADDED MY OWN STUFF BUT CREDIT WHERE CREDIT IS DUE
#
# Simple example indexing to an in-memory index and performing a search
# across multiple fields and returning an array of highlighted results.
#
# One lacking feature of Whoosh is the no-analyze option. In this example
# the SearchEngine modifies the given schema and adds a RAW field. When doc
# are added to the index only stored fields in the schema are passed to Whoosh
# along with json encoded version of the whole doc stashed in the RAW field.
#
# On query the <Hit> in the result is ignored and instead the RAW field is
# decoded containing any extra fields present in the original document.
#

# END OF OG REPO NOTES
##########################

##########################
# MY NOTES

# I'VE MOVED THE INDEX OUT OF RAM AND INTO AN ACTUAL FOLDER IN THE HOPES THAT WHEN I WANNA WHACK THIS ONLINE
# IT'S GOING TO LET ME STORE THE INDEX ON AN EC2 INSTANCE THAT PEOPLE CAN THEN QUERY
# HERE IS HOPING...

# END OF MY NOTES
##########################

# with open('search_final.json', encoding='utf-8') as raw_entities:
#     tosearch = json.load(raw_entities)

# begin_refining_results = BeginRefiningSearch()

class SearchEngine:

    def __init__(self, schema):
        self.schema = schema
        schema.add('raw', TEXT(stored=True))
        # self.ix = whoosh.index.open_dir("/mnt/files/index")
        self.ix = whoosh.index.open_dir("index")
        self.results_to_refine = []
        self.queries = []

    def query(self, q: str, fields: Sequence, highlight: bool = True) -> List[Dict]:
        search_results = []
        with self.ix.searcher() as searcher:
            results = searcher.search(MultifieldParser(
                fields, schema=self.schema).parse(q))
            for r in results:
                # print(r)
                # print("This is a result")
                d = json.loads(r['raw'])
                if highlight:
                    for f in fields:
                        if r[f] and isinstance(r[f], str):
                            d[f] = r.highlights(f) or r[f]
                search_results.append(d)
                self.results_to_refine.append(d)
            self.queries.append(q)
        return self.results_to_refine

    def filtering(self, search_field, query_term, highlight: bool = True):
        search_results = []
        with self.ix.searcher() as searcher:
            parser = QueryParser(search_field, schema=self.ix.schema)
            query = parser.parse(query_term)
            results = searcher.search(query, limit=None)
            for r in results:
                d = json.loads(r['raw'])
                if highlight:
                    if r[search_field] and isinstance(r[search_field], str):
                        d[search_field] = r.highlights(search_field) or r[search_field]
                search_results.append(d)
                self.results_to_refine.append(d)
            self.queries.append(query_term)
        return self.results_to_refine


