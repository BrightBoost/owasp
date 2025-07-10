### Exercise: SQL Injection

The current login function is vulnerable to SQL injection. A malicious user can manipulate the input to bypass authentication.

**Tasks:**
1. Try logging in with: `username = "alice'; --"` and any password.
2. Explain what this input does and why the login succeeds.
3. Rewrite the code using parameterized queries to eliminate the vulnerability.

💡 Hint: Most modern databases and libraries support parameterized queries — never build SQL statements by hand.
