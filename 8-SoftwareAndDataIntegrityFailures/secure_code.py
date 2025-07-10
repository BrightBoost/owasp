# ✅ This version avoids unsafe deserialization by using `json.loads` to safely parse user input.
# JSON is safer for untrusted data because it cannot execute arbitrary code.

import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/load")
def load():
    data = request.args.get("data")
    try:
        obj = json.loads(data)
        return f"Loaded object: {obj}"
    except json.JSONDecodeError:
        return "Invalid data", 400

if __name__ == "__main__":
    app.run(debug=False)
