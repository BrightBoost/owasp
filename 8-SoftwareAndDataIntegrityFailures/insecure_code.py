
import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route("/load")
def load():
    data = request.args.get("data")

    obj = pickle.loads(bytes.fromhex(data))
    return f"Loaded object: {obj}"

if __name__ == "__main__":
    app.run(debug=True)
