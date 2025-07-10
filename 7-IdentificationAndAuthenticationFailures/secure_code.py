# ✅ This version uses a session-based login flow. The user logs in,
# and access to the dashboard is only allowed if the session indicates authentication.

from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = "securesecret"

@app.route("/login")
def login():
    user = request.args.get("user")
    if user == "admin":
        session["user"] = user
        return "Logged in"
    return "Access denied", 401

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return f"Welcome {session['user']} to the dashboard"
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=False)
