# This version hashes the password using SHA-256 before storing it,
# so the actual password is never saved or compared directly.

import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    users[username] = hash_password(password)
    print(f"User {username} registered with hashed password")

def login(username, password):
    if users.get(username) == hash_password(password):
        return "Login successful"
    return "Login failed"

register("alice", "password123")
print(login("alice", "password123"))
