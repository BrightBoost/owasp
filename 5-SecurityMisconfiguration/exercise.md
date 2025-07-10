### Exercise: Security Misconfiguration

This web app exposes detailed error messages when an exception occurs. In a production environment, this is a serious risk.

**Tasks:**
1. Run the app and visit `/divide?a=10&b=0` — what do you see?
2. Identify why the detailed error message is dangerous.
3. Fix the code to:
   - Catch unexpected errors
   - Return a user-friendly error message
   - Disable debug mode

💡 Hint: Use a try/except block and set `debug=False` when running the app.
