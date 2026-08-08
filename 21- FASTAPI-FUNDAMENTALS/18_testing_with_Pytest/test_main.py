from fastapi.testclient import TestClient

from main import app

# Create a test client for the FastAPI application
client = TestClient(app)


# Verify the application status endpoint
def test_get_application_status():
    response = client.get("/")

    # Verify the HTTP status code
    assert response.status_code == 200

    # Verify the response body
    assert response.json() == {
        "success": True,
        "message": "API is running successfully.",
    }


# Verify the addition endpoint
def test_add_numbers():
    response = client.get(
        "/add",
        params={
            "first_number": 2,
            "second_number": 3,
        },
    )

    # Verify the HTTP status code
    assert response.status_code == 200

    # Verify the response body
    assert response.json() == {
        "success": True,
        "message": "Numbers added successfully.",
        "data": {
            "sum": 5,
        },
    }
