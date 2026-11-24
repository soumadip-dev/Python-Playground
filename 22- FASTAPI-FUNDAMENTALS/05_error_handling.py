from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

student_records = {
    "S001": {"name": "Arijit", "marks": 92, "grade": "A+"},
    "S002": {"name": "Soumadip", "marks": 88, "grade": "A"},
}


class MarksSubmissionRequest(BaseModel):
    student_id: str
    marks: int
    subject: str


# ====================
# ERROR HANDLING
# ====================


# Retrieve details of a student by their ID.
@app.get("/students/{student_id}")
def get_student_details(student_id: str):
    if student_id not in student_records:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {student_id} not found",
        )

    return student_records[student_id]


# Submit marks for a student with input validation and custom error handling.
@app.post("/submit_marks")
def submit_student_marks(submission_data: MarksSubmissionRequest):
    # Validate that the student exists.
    if submission_data.student_id not in student_records:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {submission_data.student_id} not found",
        )

    # Validate that marks are within the allowed range.
    if submission_data.marks < 0 or submission_data.marks > 100:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Marks should be between 0 and 100",
                "marks_received": submission_data.marks,
                "fix": "Provide a value between 0 and 100",
            },
        )

    # Validate that the subject name is not empty.
    if submission_data.subject.strip() == "":
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Subject name cannot be empty",
                "fix": "Provide a valid subject name",
            },
        )

    try:
        student_records[submission_data.student_id]["marks"] = submission_data.marks
        return {
            "message": "Marks submitted successfully",
            "student": student_records[submission_data.student_id]["name"],
            "subject": submission_data.subject,
            "grade": student_records[submission_data.student_id]["grade"],
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Something went wrong on server: {str(e)}",
        )


# Custome exception
class UserNotFoundException(Exception):
    def __init__(self, username: str):
        self.username = username


@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "message": f"User with username {exc.username} not found",
            "error": "UserNotFoundException",
        },
    )


@app.get("/users/{username}")
def get_user(username: str):
    for student in student_records.values():
        if student["name"].lower() == username.lower():
            return student
        raise UserNotFoundException(username)


# ====================
# STATUS CODES & CUSTOM RESPONSES
#  ====================


class User(BaseModel):
    username: str
    email: str


@app.post(
    "/create-user",
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user,
    }


@app.delete(
    "/users/{username}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(username: str):
    return


@app.put(
    "/users/{username}",
    status_code=status.HTTP_202_ACCEPTED,
)
def update_user(username: str):
    return {"message": f"Update request accepted for {username}"}
