# ❌ This app uses a hardcoded token passed through the URL for authentication.
# This is insecure because tokens in URLs can be guessed, reused, or leaked through logs or browser history.

from flask import Flask, request

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    token = request.args.get("token")
    if token == "1234":  # 🚨 Insecure: hardcoded and guessable token
        return "Welcome to the dashboard"
    return "Access denied", 401

if __name__ == "__main__":
    app.run(debug=True)
