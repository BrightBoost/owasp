
from flask import Flask, request

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    token = request.args.get("token")
    if token == "1234":
        return "Welcome to the dashboard"
    return "Access denied", 401

if __name__ == "__main__":
    app.run(debug=True)
