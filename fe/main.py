## demo app front end 
from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

#super basic Hello World Examplel
#@app.route("/")
#def hello_world():
#    return ('Hello, New Cloud World!')

# to add 
@app.route("/")
def hello_world():
    return render_template("hello_world.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

BASE_URL = 'http://35.188.104.236:8080'

@app.route("/hello_api")
def hello_api():
    # Make a request to the BE service-a API.
    response = requests.get(f"{BASE_URL}/hello")
    print(response.json())
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
