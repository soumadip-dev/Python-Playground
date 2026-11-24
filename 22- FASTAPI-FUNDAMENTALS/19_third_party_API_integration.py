from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

API_BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# Retrieve all posts from the external API
@app.get("/posts")
def get_all_posts():
    response = requests.get(API_BASE_URL)

    return {
        "success": True,
        "message": "Posts retrieved successfully.",
        "data": response.json(),
    }


# Retrieve a specific post by its ID
@app.get("/posts/{post_id}")
def get_post_by_id(post_id: int):
    response = requests.get(f"{API_BASE_URL}/{post_id}")

    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Post not found.",
        )

    return {
        "success": True,
        "message": "Post retrieved successfully.",
        "data": response.json(),
    }
