# ✅ This version disables debug mode and includes a try/except block to handle errors gracefully,
# returning only a generic message to the user.

from flask import Flask, request

app = Flask(__name__)

@app.route("/divide")
def divide():
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        return str(a / b)
    except Exception:
        return "An error occurred. Please contact support.", 400

if __name__ == "__main__":
    app.run(debug=False)  # ✅ Safe: debug mode is off
