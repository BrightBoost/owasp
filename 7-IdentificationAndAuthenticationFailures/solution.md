### Solution: Use Sessions for Authentication

**What went wrong:**
- The app used a token in the URL (e.g., ?token=1234), which can easily be guessed, shared, or leaked.

**Fix:**
- We implemented a `/login` route where users authenticate (simulated).
- Upon login, we store the username in the session.
- The `/dashboard` route checks for the session value to determine access.

This prevents unauthorized access, avoids token reuse, and keeps sensitive data out of the URL.

Replace:
```python
if token == "1234":
```

With:
```python
if "user" in session:
```