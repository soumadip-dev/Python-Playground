from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup

app = FastAPI()

NEWS_URL = "https://news.ycombinator.com/"


app = FastAPI()


@app.get("/news")
def get_latest_news(
    page: int = 1,
    limit: int = 5,
):
    try:
        response = requests.get(
            NEWS_URL,
            timeout=10,
        )
        response.raise_for_status()

    except requests.RequestException:
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve news from the source.",
        )

    soup = BeautifulSoup(
        response.text,
        "html.parser",
    )

    article_titles = []

    for article in soup.find_all(
        "span",
        class_="titleline",
    ):
        article_titles.append(article.text.strip())

    start_index = (page - 1) * limit
    end_index = start_index + limit

    return {
        "success": True,
        "message": "Latest news retrieved successfully.",
        "data": {
            "current_page": page,
            "limit": limit,
            "total_articles": len(article_titles),
            "titles": article_titles[start_index:end_index],
        },
    }
