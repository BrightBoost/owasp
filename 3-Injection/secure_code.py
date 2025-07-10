# This version uses parameterized queries, which separates code from data.
# This prevents SQL injection by ensuring user input is treated as data only.

import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users (username TEXT, password TEXT)")
c.execute("INSERT INTO users VALUES (?, ?)", ("alice", "password123"))

def login(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print("Executing safe query")
    c.execute(query, (username, password))
    return "Login successful" if c.fetchone() else "Login failed"

print(login("alice", "password123"))
print(login("alice'; --", "irrelevant"))  # ✅ Injection attempt fails
