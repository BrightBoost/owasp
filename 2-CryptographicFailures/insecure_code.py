
users = {}

def register(username, password):
    users[username] = password 
    print(f"User {username} registered with password: {password}")

def login(username, password):
    if users.get(username) == password:
        return "Login successful"
    return "Login failed"

register("alice", "password123")
print(login("alice", "password123"))
