from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_application_status():
    return {
        "success": True,
        "message": "API is running successfully.",
    }


@app.get("/add")
def add_numbers(first_number: int, second_number: int):
    return {
        "success": True,
        "message": "Numbers added successfully.",
        "data": {
            "sum": first_number + second_number,
        },
    }
