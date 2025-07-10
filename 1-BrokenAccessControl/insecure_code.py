from flask import Flask, request

app = Flask(__name__)

# Dummy data
users = {
    "1": {"id": 1, "name": "Alice"},
    "2": {"id": 2, "name": "Bob"}
}

@app.route("/profile")
def profile():
    user_id = request.args.get("user_id")
    return users.get(user_id, {"error": "User not found"})

if __name__ == "__main__":
    app.run(debug=True)
