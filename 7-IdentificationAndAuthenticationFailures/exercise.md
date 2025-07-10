### Exercise: Authentication Failures

The current dashboard uses a hardcoded URL token to "secure" access. This is a weak and unsafe method.

**Tasks:**
1. Visit `/dashboard?token=1234` — notice how anyone with the token can access it.
2. Explain why this token approach is insecure.
3. Implement a login system where only logged-in users (via session) can access `/dashboard`.

💡 Hint: Use Flask sessions and check whether the user is logged in by checking the session state.
