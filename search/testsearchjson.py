import json
import whoosh
from typing import Dict, List, Sequence

from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import MultifieldParser
from whoosh.filedb.filestore import RamStorage
from whoosh.analysis import StemmingAnalyzer

with open('DiscordDataTest.json', encoding='utf-8') as raw_entities:
    tosearch = json.load(raw_entities)


class SearchEngine:
    
    def __init__(self, schema):
        self.schema = schema
        schema.add('raw', TEXT(stored=True))
        self.ix = RamStorage().create_index(self.schema)

    def index_documents(self, docs: Sequence):
        writer = self.ix.writer()
        for doc in docs:
                d = {k: v for k,v in docs[doc].items() if k in self.schema.stored_names()}
                # print("I am printing d")
                d['raw'] = json.dumps(docs[doc]) # raw version of all of doc
                writer.add_document(**d)
        writer.commit(optimize=True)

    def get_index_size(self) -> int:
        return self.ix.doc_count_all()

    def query(self, q: str, fields: Sequence, highlight: bool=True) -> List[Dict]:
        search_results = []
        with self.ix.searcher() as searcher:
            results = searcher.search(MultifieldParser(fields, schema=self.schema).parse(q))
            print(results)
            for r in results:
                print(r['raw'])
                print("rwar")
                d = json.loads(r['raw'])
                if highlight:
                    for f in fields:
                        if r[f] and isinstance(r[f], str):
                            d[f] = r.highlights(f) or r[f]

                search_results.append(d)

        return search_results


if __name__ == '__main__':

    docs = tosearch

    schema = Schema(
        episode_title=ID(stored=True),
        topics=TEXT(stored=True, analyzer=StemmingAnalyzer()),
        people=TEXT(stored=True, analyzer=StemmingAnalyzer()),
        alex_says=KEYWORD(stored=True),
        deep_dive_topics=KEYWORD(stored=True),
        deep_dive_aliases=KEYWORD(stored=True)
    )

searchtest = SearchEngine(schema)
searchtest.index_documents(docs)

# print(docs)

print(f"indexed {searchtest.get_index_size()} documents")

fields_to_search = ["episode_title", "topics"]

for q in ["2017"]:
    print(f"Query:: {q}")
    print("\t", searchtest.query(q, fields_to_search, highlight=True))
    print("-"*70)