# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "flask",
#     "requests",
# ]
# ///
from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

if __name__ == "__main__" :
    app.run()