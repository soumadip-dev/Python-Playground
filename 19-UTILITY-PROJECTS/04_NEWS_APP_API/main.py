from datetime import datetime, timedelta
import requests


search_topic = input("Enter the type of news you are interested in today: ").strip()


api_key = "04256bf72f4d4ffda934362796235452"


start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")


request_url = (
    f"https://newsapi.org/v2/everything?"
    f"q={search_topic}&from={start_date}&sortBy=publishedAt&apiKey={api_key}"
)


response = requests.get(request_url)
response_data = response.json()
articles_list = response_data.get("articles", [])


# Print article titles and URLs
for article in articles_list:
    article_title = article.get("title", "No title available")
    article_url = article.get("url", "No URL available")

    print("Title:", article_title)
    print("URL:", article_url)
    print("*" * 50)
