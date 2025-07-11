# 🧠 Extra Challenges: Secure Coding & OWASP Top 10

Want to push yourself beyond the workshop? Try these bonus challenges! Each one helps you deepen your secure coding skills through real-world scenarios.

You don’t have to do them all — just pick the one(s) that interest you most.

Have fun, think like a hacker _and_ a defender, and remember:

> **Security is not a feature — it’s a habit.**

For more (interactive explanations):
[Hacksplaining](https://www.hacksplaining.com/lessons)

---

## 🧃 1. OWASP Juice Shop

A vulnerable e-commerce app designed for hacking practice. Try to exploit known OWASP Top 10 issues — and then see if you can fix them!

🔗 https://owasp.org/www-project-juice-shop/

✅ **Try this:**

- Run Juice Shop locally (Docker or Node)
- Try to:
  - View another user’s account (A01: Broken Access Control)
  - Manipulate a SQL query (A03: Injection)
  - Find hardcoded secrets (A08: Integrity)

---

## 🧀 2. Google Gruyere (Cheesy but Effective)

A deliberately insecure web app from Google that teaches web security through hands-on exploration.

🔗 https://google-gruyere.appspot.com

✅ **Try this:**

- Complete the built-in challenges
- Focus on XSS, CSRF, and auth flaws

---

## 🧩 3. Build It Right: Secure Login System

**Goal:** Build a basic login system with proper security.

✅ **Must-haves:**

- Password hashing (e.g. bcrypt or SHA-256)
- Session-based login/logout
- No credentials in URLs
- Access control: authenticated users only

💡 Use Flask, Express.js, or a language of your choice!

---

## 🏹 4. Capture-the-Flag: Fix & Defend

Set up a small vulnerable app (e.g. from [Root Me](https://www.root-me.org/) or [TryHackMe](https://tryhackme.com/)).

✅ **Challenge:**

1. Find the vulnerability (e.g. broken access control or injection)
2. Exploit it to get a flag
3. Fix it in code
4. Retest to confirm the patch

---

## 🤖 5. Bonus Brain-Buster: AI Security

Imagine you're building a chatbot, form filler, or code assistant. What are the risks?

✅ **Discuss or explore:**

- Prompt injection
- Sensitive data logging
- Over-trusting user input
- Lack of access restrictions

💬 Bonus: Draft a secure-by-design plan for your AI app
