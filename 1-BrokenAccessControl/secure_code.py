from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = "secret"

# Dummy data
users = {
    "1": {"id": 1, "name": "Alice"},
    "2": {"id": 2, "name": "Bob"}
}

@app.route("/login")
def login():
    session["user_id"] = "1"  # Assume user 1 is logged in
    return "Logged in"

@app.route("/profile")
def profile():
    user_id = session.get("user_id")
    if not user_id:
        return {"error": "Not authenticated"}, 401
    return users.get(user_id, {"error": "User not found"})

if __name__ == "__main__":
    app.run(debug=True)
