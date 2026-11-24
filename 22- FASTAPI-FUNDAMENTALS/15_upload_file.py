import os
import shutil

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Step 1: Create the uploads directory if it does not exist
UPLOADS_DIR = "uploads"

if not os.path.exists(UPLOADS_DIR):
    os.makedirs(UPLOADS_DIR)

# Step 2: Configure static file serving
# Uploaded files will be accessible at:
# http://localhost:8000/files/<filename>
app.mount(
    "/files",
    StaticFiles(directory=UPLOADS_DIR),
    name="files",
)


# Step 3: Upload file API
@app.post("/upload")
def upload_file(
    file: UploadFile = File(...),
):
    filename = file.filename

    if not filename:
        raise HTTPException(
            status_code=400,
            detail="No file was provided.",
        )

    file_path = os.path.join(
        UPLOADS_DIR,
        filename,
    )

    with open(file_path, "wb") as uploaded_file:
        shutil.copyfileobj(
            file.file,
            uploaded_file,
        )

    return {
        "success": True,
        "message": "File uploaded successfully.",
        "data": {
            "filename": filename,
            "file_url": f"http://localhost:8000/files/{filename}",
        },
    }


# Step 4: Get uploaded file details API
@app.get("/files/{filename}")
def get_file_details(
    filename: str,
):
    file_path = os.path.join(
        UPLOADS_DIR,
        filename,
    )

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found.",
        )

    return {
        "success": True,
        "message": "File retrieved successfully.",
        "data": {
            "filename": filename,
            "file_url": f"http://localhost:8000/files/{filename}",
        },
    }


# Step 5: Health check API
@app.get("/")
def get_application_status():
    return {
        "success": True,
        "message": "File upload service is running.",
    }
