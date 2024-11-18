import time
import json

from tqdm import tqdm
from typing import List
from pprint import pprint
from elasticsearch import Elasticsearch


def index_data(documents: List[dict]):
    index_name = 'apod'
    es = _get_es_client(max_retries=5, sleep_time=5)
    _create_index(es=es, index_name=index_name)
    _insert_documents(es=es, index_name=index_name, documents=documents)
    pprint(f'Indexed {len(documents)} documents into Elasticsearch index "{index_name}"')


def _get_es_client(max_retries: int = 5, sleep_time: int = 5) -> Elasticsearch:
    i = 0
    while i < max_retries:
        try:
            es = Elasticsearch('http://localhost:9200')
            client_info = es.info()
            pprint('Connected to Elasticsearch!')
            pprint(f'Cluster info:\n{client_info}')
            return es
        except Exception:
            pprint('Could not connect to Elasticsearch, retrying...')
            time.sleep(sleep_time)
            i += 1
    raise ConnectionError("Failed to connect to Elasticsearch after multiple attempts.")


def _create_index(es: Elasticsearch, index_name: str):
    es.indices.delete(index=index_name, ignore_unavailable=True)
    es.indices.create(index=index_name)


def _insert_documents(es: Elasticsearch, index_name: str, documents: List[dict]):
    operations = []
    for document in tqdm(documents, total=len(documents), desc='Indexing documents'):
        operations.append({'index': {'_index': index_name}})
        operations.append(document)
    return es.bulk(operations=operations)


if __name__ == '__main__':
    with open('../../data/apod.json') as f:
        documents = json.load(f)

    index_data(documents=documents)
