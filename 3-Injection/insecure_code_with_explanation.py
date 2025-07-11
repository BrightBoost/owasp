# This version builds SQL queries by directly inserting user input into the query string.
# This makes the app vulnerable to SQL injection attacks — malicious users can manipulate
# the query to bypass login or extract data.

import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users (username TEXT, password TEXT)")
c.execute("INSERT INTO users VALUES ('alice', 'password123')")

def login(username, password):
    # 🚨 Insecure: directly interpolating user input into SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)
    c.execute(query)
    return "Login successful" if c.fetchone() else "Login failed"

print(login("alice", "password123"))
print(login("alice'; --", "irrelevant"))  # 🚨 This bypasses the password check
