from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Frontend application URL
allowed_origins = [
    "http://localhost:5173",
]

# Configure Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Allow requests from the specified frontend origin
    allow_credentials=True,  # Allow cookies and authentication credentials
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, PATCH, DELETE, etc.)
    allow_headers=["*"],  # Allow all request headers
)


@app.get("/")
def get_application_status():
    return {
        "success": True,
        "message": "API is running successfully.",
    }
