from fastapi import FastAPI
import sqlite3

# Initialize FastAPI app
app = FastAPI()

# Create/connect to SQLite database
# check_same_thread=False allows SQLite to be used with FastAPI (multi-threaded environment)
connection = sqlite3.connect("database.db", check_same_thread=False)
cursor = connection.cursor()

# Create "todos" table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed BOOLEAN DEFAULT 0
)
""")

# Save changes to database
connection.commit()


@app.get("/")
def root():
    return {
        "status": "success",
        "message": "FastAPI application is running and SQLite database is connected successfully.",
    }
