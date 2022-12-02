import json
import whoosh
from typing import Dict, List, Sequence

from refiningresults import RefiningResults
from beginresultrefining import BeginRefiningSearch

from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import MultifieldParser
from whoosh.filedb.filestore import RamStorage
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import QueryParser

from whoosh import query
from whoosh.query import Term

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

with open('reformatted_discord_data.json', encoding='utf-8') as raw_entities:
    tosearch = json.load(raw_entities)

pass_to_refining = RefiningResults()
begin_refining_results = BeginRefiningSearch()

class SearchEngine:

    def __init__(self, schema):
        self.schema = schema
        schema.add('raw', TEXT(stored=True))
        self.ix = RamStorage().create_index(self.schema)
        self.testing_results = []

    def index_documents(self, docs: Sequence):
        writer = self.ix.writer()
        for doc in docs:
            d = {k: v for k, v in docs[doc].items(
            ) if k in self.schema.stored_names()}
            d['raw'] = json.dumps(docs[doc])  # raw version of all of doc
            writer.add_document(**d)
        writer.commit(optimize=True)

    def get_index_size(self) -> int:
        return self.ix.doc_count_all()

    def get_testing_size(self):
        print(len(self.testing_results))

    def query(self, q: str, fields: Sequence, highlight: bool = True) -> List[Dict]:
        search_results = []
        with self.ix.searcher() as searcher:
            results = searcher.search(MultifieldParser(
                fields, schema=self.schema).parse(q))
            for r in results:
                d = json.loads(r['raw'])
                if highlight:
                    for f in fields:
                        if r[f] and isinstance(r[f], str):
                            d[f] = r.highlights(f) or r[f]

                search_results.append(d)
                self.testing_results.append(d)
        # begin_refining_results.begin_refining(fields, search_results, q)
        return search_results

    def testfilter(self, search_field, query_term):
        search_results = []
        with self.ix.searcher() as searcher:
            parser = QueryParser(search_field, schema=self.ix.schema)
            query = parser.parse(query_term)
            results = searcher.search(query, limit=None)
            print(results, len(results))
            for r in results:
                d = json.loads(r['raw'])
                search_results.append(d)
        return search_results


if __name__ == '__main__':

    docs = tosearch

    schema = Schema(
        episode_title=ID(stored=True),
        topics_tostring=TEXT(stored=True, analyzer=StemmingAnalyzer()),
        topics=KEYWORD(stored=True),
        people_tostring=TEXT(stored=True, analyzer=StemmingAnalyzer()),
        people=KEYWORD(stored=True),
        alex_says_tostring=TEXT(stored=True, analyzer=StemmingAnalyzer()),
        alex_says=KEYWORD(stored=True),
        deep_dive_topics_tostring=TEXT(
            stored=True, analyzer=StemmingAnalyzer()),
        deep_dive_topics=KEYWORD(stored=True),
        deep_dive_aliases_tostring=TEXT(
            stored=True, analyzer=StemmingAnalyzer())
    )

    engine = SearchEngine(schema)
    engine.index_documents(docs)

    print(f"indexed {engine.get_index_size()} documents")

    fields_to_search = ["topics_tostring", "deep_dive_topics_tostring",
                        "people_tostring", "alex_says_tostring"]

    for q in ["PJW", "Mark Dice", "weeny"]:
        # print(f"Query:: {q}")
        # print("\t", engine.query(q, fields_to_search, highlight=True))
        engine.query(q, fields_to_search, highlight=True)
        print(len(engine.testing_results))
        print("-"*70)
    begin_refining_results.begin_refining(fields_to_search, engine.testing_results, q)

    # print(engine.testfilter("topics_tostring", "Andy in Kansas"))
