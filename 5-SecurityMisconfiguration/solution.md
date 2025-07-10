### Solution: Handle Errors Gracefully and Disable Debug Mode

Detailed stack traces are useful during development but dangerous in production.
They can leak file paths, code structure, or even credentials.

**What we fixed:**
- Wrapped logic in a `try/except` block to catch errors like division by zero.
- Returned a generic error message to avoid leaking internals.
- Disabled Flask's debug mode.

Bad:
```python
app.run(debug=True)
```

Good:
```python
app.run(debug=False)
```

And:
```python
except Exception:
    return "An error occurred. Please contact support.", 400
```