import os

from flask import Flask, jsonify
# from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def index():
    return jsonify({'message': 'Hello from service-a'})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))