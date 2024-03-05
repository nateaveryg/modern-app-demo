## demo app front end 
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('Hello, World!')

# to add later
#@app.route("/")
#def hello_world():
#    return render_template("hello_world.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))