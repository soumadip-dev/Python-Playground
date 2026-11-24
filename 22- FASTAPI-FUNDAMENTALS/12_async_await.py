import asyncio
import time

# ------------------------------------------------------------------
# Example Synchronous Function
# ------------------------------------------------------------------
# def fetch_greeting_message():
#     time.sleep(3)
#     return "Hello from synchronous code"


# ------------------------------------------------------------------
# Example Asynchronous Function
# ------------------------------------------------------------------
# async def fetch_greeting_message():
#     await asyncio.sleep(3)
#     return "Hello from asynchronous code"


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_health_status():
    # Simulate an asynchronous I/O-bound operation
    await asyncio.sleep(3)

    return {
        "success": True,
        "message": "API is running successfully.",
    }
