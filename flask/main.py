from flask import Flask

app = Flask(__name__)

@app.route("/")
async def root():
    return {"message": "Hello World"}