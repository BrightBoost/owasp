# ❌ This app uses Python's `pickle` module to deserialize user input.
# If an attacker sends a maliciously crafted payload, it could execute arbitrary code on the server.

import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route("/load")
def load():
    data = request.args.get("data")
    # 🚨 Insecure: untrusted input passed directly into `pickle.loads`
    obj = pickle.loads(bytes.fromhex(data))
    return f"Loaded object: {obj}"

if __name__ == "__main__":
    app.run(debug=True)
