from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173",
     "https://vue-js-with-flask-backend-1.onrender.com"])

items = [{"id": 1, "name": "Apple"}, {"id":2, "name":"Banana"}]

@app.route("/items", methods= ["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_item():
    item = request.get_json()
    items.append(item)
    return jsonify(item), 201

if __name__ == "__main__":
    app.run(debug=True)


