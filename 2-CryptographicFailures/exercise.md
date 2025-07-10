### Exercise: Cryptographic Failures

The current implementation stores user passwords in plain text. This is a major security risk.

**Tasks:**
1. Identify the cryptographic flaw in the current implementation.
2. Update the code to securely store and compare passwords using hashing.
3. Ensure that users can still register and log in — but now securely.

💡 Hint: Use a hash function like SHA-256 (or in real life, bcrypt) to store only the hashed version of the password.
