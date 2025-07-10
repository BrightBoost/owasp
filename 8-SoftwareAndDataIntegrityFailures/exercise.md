### Exercise: Unsafe Deserialization

This app currently uses `pickle` to deserialize data sent by the user — a major security risk.

**Tasks:**
1. Read the code and explain what `pickle.loads()` does.
2. Research why deserializing untrusted input with `pickle` is dangerous.
3. Replace the deserialization logic to use `json.loads()` instead, which safely handles user data.

💡 Hint: `pickle` can execute any code embedded in the payload. JSON cannot.
