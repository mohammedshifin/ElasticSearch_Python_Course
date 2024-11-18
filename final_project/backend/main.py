from fastapi import FastAPI
from config import INDEX_NAME
from utils import get_es_client


app = FastAPI()


@app.get("/api/v1/search/")
async def search(search_query: str, skip: int = 0, limit: int = 10) -> dict:
    es = get_es_client(max_retries=5, sleep_time=5)
    response = es.search(
        index=INDEX_NAME,
        body={
            "query": {
                "multi_match": {
                    "query": search_query,
                    "fields": ["title", "explanation"]
                }
            },
            "from": skip,
            "size": limit
        },
        filter_path=["hits.hits._source,hits.hits._score"]
    )
    hits = response["hits"]["hits"]
    return {"hits": hits}
