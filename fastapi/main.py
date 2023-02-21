from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
import mysql.connector

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def users() -> List[dict]:
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="mysql-test",
        user="test-user",
        password="test-user-password",
        database="test",
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor(dictionary=True)

    # Execute a SELECT statement to retrieve all users from the table
    query = "SELECT * FROM users"
    cursor.execute(query)

    # Fetch all rows and return them as a list of dictionaries
    rows = cursor.fetchall()
    users = [dict(row) for row in rows]

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    # Return the list of users as a JSON response
    return JSONResponse(content=users, status_code=200)