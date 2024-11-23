from config import INDEX_NAME
from utils import get_es_client

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/search/")
async def search(search_query: str, skip: int = 0, limit: int = 10) -> dict:
    try:
        es = get_es_client(max_retries=1, sleep_time=0)
        
        response = es.search(
            index=INDEX_NAME,
            body={
                "query": {
                    "multi_match": {
                        "query": search_query,
                        "fields": ["title", "explanation"],
                    }
                },
                "from": skip,
                "size": limit
            },
            filter_path=["hits.hits._source,hits.hits._score"]
        )
        if not response:
            return {"hits": []}
        
        hits = response["hits"]["hits"]
        return {"hits": hits}
    except ConnectionError:
        error_message = "Could not connect to Elasticsearch, make sure that the cluster is up and running."
        return HTMLResponse(content=error_message, status_code=500)
