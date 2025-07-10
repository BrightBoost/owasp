### Solution: Never Deserialize Untrusted Input with `pickle`

**Why this is dangerous:**
- `pickle.loads()` can evaluate arbitrary Python objects.
- A malicious user can craft a payload that executes code upon loading.

**Fix:**
- Switch to `json.loads()` which parses structured data (e.g., dictionaries, lists) safely.

Unsafe:
```python
pickle.loads(bytes.fromhex(data))
```

Safe:
```python
json.loads(data)
```

This eliminates the risk of arbitrary code execution from user-controlled input.
