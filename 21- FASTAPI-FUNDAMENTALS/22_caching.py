from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup
import time

app = FastAPI()

# Cache storage
cached_news = []
last_cache_update = 0


@app.get("/news")
def get_latest_news():
    global cached_news, last_cache_update

    request_start_time = time.time()

    # Refresh cached data every 60 seconds
    if time.time() - last_cache_update > 60:
        print("Fetching fresh news data...")

        NEWS_URL = "https://news.ycombinator.com/"

        try:
            response = requests.get(
                NEWS_URL,
                timeout=10,
            )
            response.raise_for_status()

        except requests.RequestException:
            raise HTTPException(
                status_code=500,
                detail="Failed to fetch news from the source.",
            )

        soup = BeautifulSoup(
            response.text,
            "html.parser",
        )

        cached_news = [
            item.text
            for item in soup.find_all(
                "span",
                class_="titleline",
            )
        ]

        last_cache_update = time.time()

    else:
        print("Returning cached news data...")

    request_end_time = time.time()
    response_time = round(
        request_end_time - request_start_time,
        2,
    )

    print(f"Response time: {response_time} seconds")

    return {
        "success": True,
        "message": "News fetched successfully.",
        "response_time": response_time,
        "data": {
            "titles": cached_news[:5],
        },
    }
