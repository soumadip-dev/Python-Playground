from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# =========================
# SIMPLE BASE MODEL
# =========================


class VoterDetails(BaseModel):
    name: str
    email: str
    phone: str
    age: int
    voter_id: int


@app.post("/voter")
def check_voter_eligibility(voter: VoterDetails):
    is_underage = voter.age < 18

    voter_status = "Eligible to vote" if not is_underage else "Not eligible to vote"

    return {
        "message": voter_status,
        "voter_details": voter,
    }


# =========================
# NESTED BASE MODEL
# =========================


class Address(BaseModel):
    city: str
    state: str
    postal_code: int


class UserProfile(BaseModel):
    full_name: str
    email: str
    age: int
    voter_id: int
    address: Address


@app.post("/user/profile")
def create_user_profile(profile: UserProfile):
    is_eligible_to_vote = profile.age >= 18

    voter_status = "Eligible to vote" if is_eligible_to_vote else "Not eligible to vote"

    return {
        "message": "User profile created successfully.",
        "user_data": profile,
        "voter_status": voter_status,
    }
