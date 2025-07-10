### Solution: Enforce Access Control Based on Session

The vulnerability allows users to view other people’s data by changing the `user_id` in the URL.

**What we fixed:**
- Removed reliance on `request.args.get("user_id")`
- Used `session.get("user_id")` to determine the currently logged-in user

```python
user_id = session.get("user_id")

This prevents Insecure Direct Object Reference (IDOR) attacks by ensuring users can only access their own data.
 