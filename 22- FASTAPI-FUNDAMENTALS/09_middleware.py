from fastapi import FastAPI, Request
import time

app = FastAPI()


@app.middleware("http")
async def request_logging_middleware(request: Request, call_next):
    start_time = time.time()

    print(f"[REQUEST START] Method={request.method} Path={request.url.path}")

    response = await call_next(request)
    process_time = time.time() - start_time

    print(
        f"[REQUEST END] Method={request.method} "
        f"Path={request.url.path} "
        f"Status={response.status_code} "
        f"Duration={process_time:.4f}s"
    )

    return response
