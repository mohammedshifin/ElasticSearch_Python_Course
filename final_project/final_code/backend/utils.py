import time

from pprint import pprint
from elasticsearch import Elasticsearch

def get_es_client(max_retries: int = 1, sleep_time: int = 5) -> Elasticsearch:
    ca_certs = "C:/ELK stack/elasticsearch-8.17.2/config/certs/http_ca.crt"
    es_config = {
        "hosts": ["https://localhost:9200"], 
        "ca_certs": ca_certs,
        "basic_auth": ("elastic", "wHJp0zW7Qo9R-I6Uaeg6"), 
        "verify_certs": True,
        "timeout": 30,
        "retry_on_timeout": True,
        "max_retries": 3
    }
    
    i = 0
    while i < max_retries:
        try:
            es = Elasticsearch(**es_config)
            if es.ping():
                print("Connected to Elasticsearch!")
                return es
            else:
                print("Could not ping Elasticsearch server")
        except Exception as e:
            print(f'Connection failed: {str(e)}')
            time.sleep(sleep_time)
            i += 1
    
    raise ConnectionError("Failed to connect to Elasticsearch after multiple attempts.")