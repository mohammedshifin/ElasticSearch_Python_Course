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
        response = perform_search(es=es, search_query=search_query, skip=skip, limit=limit)

        if not response:
            return {"hits": [], "max_pages": 0, "docs_per_year": {}}

        total_hits = get_total_hits(response)
        max_pages = calculate_max_pages(total_hits, limit)
        docs_per_year = extract_docs_per_year(response)

        return {
            "hits": response["hits"]["hits"],
            "max_pages": max_pages,
            "docs_per_year": docs_per_year,
        }
    except ConnectionError:
        return handle_connection_error()


def perform_search(es, search_query: str, skip: int, limit: int) -> dict:
    """
    Executes the search query on Elasticsearch.
    """
    return es.search(
        index=INDEX_NAME,
        body={
            "query": {
                "multi_match": {
                    "query": search_query,
                    "fields": ["title", "explanation"],
                }
            },
            "from": skip,
            "size": limit,
            "aggs": {
                "docs_per_year": {
                    "date_histogram": {
                        "field": "date",
                        "calendar_interval": "year",  # Group by year
                        "format": "yyyy"             # Format the year in the response
                    }
                }
            },
        },
        filter_path=[
            "hits.hits._source",
            "hits.hits._score",
            "hits.total",
            "aggregations.docs_per_year"
        ]
    )


def get_total_hits(response: dict) -> int:
    return response["hits"]["total"]["value"]


def calculate_max_pages(total_hits: int, limit: int) -> int:
    return (total_hits + limit - 1) // limit


def extract_docs_per_year(response: dict) -> dict:
    aggregations = response.get("aggregations", {})
    docs_per_year = aggregations.get("docs_per_year", {})
    buckets = docs_per_year.get("buckets", [])
    return {bucket["key_as_string"]: bucket["doc_count"] for bucket in buckets}


def handle_connection_error() -> HTMLResponse:
    error_message = "Could not connect to Elasticsearch, make sure that the cluster is up and running."
    return HTMLResponse(content=error_message, status_code=500)
