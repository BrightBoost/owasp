

import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users (username TEXT, password TEXT)")
c.execute("INSERT INTO users VALUES ('alice', 'password123')")

def login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)
    c.execute(query)
    return "Login successful" if c.fetchone() else "Login failed"

print(login("alice", "password123"))
print(login("alice'; --", "irrelevant"))  
