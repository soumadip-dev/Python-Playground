from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


# ============================================================
# Dependency Injection and Reusable Authentication Logic
# ============================================================
def get_current_user():
    return {"username": "Soumadip"}


@app.get("/profile")
def get_profile(current_user: dict = Depends(get_current_user)):
    return current_user


@app.get("/dashboard")
def get_dashboard(current_user: dict = Depends(get_current_user)):
    return current_user


# ============================================================
# Header-Based Token Authentication
# ============================================================


def verify_token(token: str = Header(default=None)):
    if token != "secret-token":
        raise HTTPException(status_code=401, detail="Unauthorized access")

    return {"username": "Soumadip", "status": "Authenticated"}


@app.get("/protected")
def get_protected_data(current_user: dict = Depends(verify_token)):
    return {"message": "Secure data accessed successfully.", "user": current_user}
