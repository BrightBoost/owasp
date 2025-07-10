### Solution: Use Parameterized Queries

The vulnerability happens because user input is directly embedded into the SQL query string.

**Fix:**
Use parameterized queries, which treat input as values, not executable SQL.

Unsafe:
```python
query = f"SELECT * FROM users WHERE username = '{username}'"
```

Safe:
```python
query = "SELECT * FROM users WHERE username = ?"
c.execute(query, (username,))
```

This protects against malicious input such as alice'; --.
