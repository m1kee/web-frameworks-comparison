from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/")
async def root():
    return {"message": "Hello World"}

# define route to get all users
@app.route("/users")
def get_users():
    mydb = mysql.connector.connect(
        host="mysql-test",
        user="test-user",
        password="test-user-password",
        database="test",
        port=3306
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users")
    users = mycursor.fetchall()
    return jsonify(users)