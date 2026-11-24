from fastapi import Depends, HTTPException, Request, Query, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
import time

import models
import database
import schemas
from database import SessionLocal
from envConfig import settings
from auth import create_access_token, verify_access_token

models.Base.metadata.create_all(bind=database.engine)


# Cache storage variables
cached_blogs = None
last_cache_update = 0
CACHE_TIME = 60  # Cache expires after 60 seconds


# Provide a database session for each request. The session is automatically closed after the request completes.
def get_db():
    db: Session = SessionLocal()

    try:
        yield db

    finally:
        db.close()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


# Limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


# Error handler for rate limiting
@app.exception_handler(RateLimitExceeded)
def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "success": False,
            "message": "Too many requests. Please try again later.",
        },
    )


# Authentication(login) endpoint
@app.post("/login", response_model=schemas.LoginResponse)
def login():
    return {
        "success": True,
        "message": "Login successful.",
        "access_token": create_access_token({"user": "admin"}),
        "token_type": "bearer",
    }


# Configure Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/")
def get_application_status():
    return {
        "success": True,
        "message": "Blog API is running successfully.",
    }


# Create a new blog post
@app.post("/blogs", response_model=schemas.BlogResponse)
@limiter.limit("5/minute")
def create_blog(
    request: Request,
    blog: schemas.BlogCreate,
    db: Session = Depends(get_db),
    user=Depends(verify_access_token),
):
    global cached_blogs

    new_blog = models.Blog(
        title=blog.title,
        content=blog.content,
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    # Clear cache after creating a blog
    cached_blogs = None

    return {
        "success": True,
        "message": "Blog created successfully.",
        "data": new_blog,
    }


# Retrieve all blogs
@app.get("/blogs", response_model=schemas.BlogListResponse)
@limiter.limit("5/minute")
def get_blogs(
    request: Request,
    db: Session = Depends(get_db),
    page: int = 1,
    limit: int = 5,
    search: str = Query(""),
):
    global cached_blogs, last_cache_update

    # Refresh cache every 60 seconds
    if cached_blogs is None or time.time() - last_cache_update > CACHE_TIME:
        print("Fetching fresh blogs from database...")

        cached_blogs = db.query(models.Blog).all()
        last_cache_update = time.time()

    else:
        print("Returning cached blogs...")

    # Apply search on cached data
    filtered_blogs = cached_blogs

    if search:
        filtered_blogs = [
            blog for blog in cached_blogs if search.lower() in blog.title.lower()
        ]

    # Apply pagination
    start_index = (page - 1) * limit
    end_index = start_index + limit

    return {
        "success": True,
        "message": "Blogs retrieved successfully.",
        "page": page,
        "limit": limit,
        "data": filtered_blogs[start_index:end_index],
    }


# Retrieve a single blog
@app.get("/blogs/{blog_id}", response_model=schemas.BlogResponse)
@limiter.limit("5/minute")
def get_blog(
    request: Request,
    blog_id: int,
    db: Session = Depends(get_db),
):
    blog = db.query(models.Blog).filter_by(id=blog_id).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found",
        )

    return {
        "success": True,
        "message": "Blog retrieved successfully.",
        "data": blog,
    }


# Update a blog
@app.put("/blogs/{blog_id}", response_model=schemas.BlogResponse)
@limiter.limit("5/minute")
def update_blog(
    request: Request,
    blog_id: int,
    blog_data: schemas.BlogCreate,
    db: Session = Depends(get_db),
    user=Depends(verify_access_token),
):
    global cached_blogs

    blog = db.query(models.Blog).filter_by(id=blog_id).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found",
        )

    blog.title = blog_data.title
    blog.content = blog_data.content

    db.commit()
    db.refresh(blog)

    # Clear cache after updating a blog
    cached_blogs = None

    return {
        "success": True,
        "message": "Blog updated successfully.",
        "data": blog,
    }


# Delete a blog
@app.delete("/blogs/{blog_id}", response_model=schemas.BlogResponse)
@limiter.limit("5/minute")
def delete_blog(
    request: Request,
    blog_id: int,
    db: Session = Depends(get_db),
    user=Depends(verify_access_token),
):
    global cached_blogs

    blog = db.query(models.Blog).filter_by(id=blog_id).first()

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found",
        )

    db.delete(blog)
    db.commit()

    # Clear cache after deleting a blog
    cached_blogs = None

    return {
        "success": True,
        "message": "Blog deleted successfully.",
        "data": blog,
    }
