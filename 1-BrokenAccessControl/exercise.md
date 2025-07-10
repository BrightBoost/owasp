### Exercise: Broken Access Control

The current implementation allows any user to view any other user's profile by modifying the `user_id` parameter in the URL.

**Tasks:**
1. Run the application and visit `/profile?user_id=2` — what do you see?
2. Explain why this is a security issue.
3. Fix the code so that only the logged-in user can view their own profile.

💡 Hint: Use session-based authentication and restrict access to the session’s `user_id`.
