from bs4 import BeautifulSoup
import requests

# Fetch and parse the Indian Express homepage

url = "https://indianexpress.com/"
response = requests.get(url)

soup = BeautifulSoup(
    response.text,
    "html.parser",
)

if soup.title:
    print(soup.title.text.strip())
else:
    print("No page title found.")


from fastapi import FastAPI

app = FastAPI()


# Fetch and parse the Indian Express homepage
@app.get("/news")
def get_latest_news():
    # Fetch the Indian Express homepage
    url = "https://indianexpress.com/"
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(
        response.text,
        "html.parser",
    )

    news_titles = []

    # Extract the latest news headlines
    for article in soup.find_all(
        "a",
        class_="article-click topblockNews__sidebarLink",
    ):
        news_titles.append(article.text.strip())

    return {
        "success": True,
        "message": "Latest news retrieved successfully.",
        "data": {
            "titles": news_titles[:5],
        },
    }
