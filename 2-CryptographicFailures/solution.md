### Solution: Store Hashed Passwords

Plain text password storage is dangerous — anyone who accesses the database can see all user passwords.

**How we fixed it:**
- We used SHA-256 to hash the password before storing it.
- During login, we hash the input and compare it to the stored hash.

```python
users[username] = hashlib.sha256(password.encode()).hexdigest()
