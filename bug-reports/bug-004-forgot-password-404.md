# 🐞 Bug Report: Forgot password link returns 404

**Bug ID:** BUG-004  
**Reported By:** Walter Lam  
**Date:** 2025-08-13  
**Severity:** Medium  
**Priority:** P2

---

## 📝 Summary
Clicking **Forgot password?** on the login screen routes to a missing page and returns **404**.

---

## 🔄 Steps to Reproduce
1. Open `/login`.
2. Click **Forgot password?**.
3. Observe the destination and result.

---

## ✅ Expected Result
User is taken to a **Password reset** screen (HTTP **200**) containing an email input (or the flow kicks off with clear guidance).

---

## ❌ Actual Result
Navigation lands on a non-existent route (e.g., `/forgot`) and returns **404 Not Found**.

---

## 🧭 Environment
- **OS:** Windows 11  
- **Browser:** Chrome 126 (64-bit)  
- **App:** Local demo (`file:///…/manual-qa-sample/login.html`) — no public URL

---

## 🔍 Technical Details
- Console/Network: navigation to a missing path; **404** returned.
- No JavaScript runtime errors observed.

---

## 📎 Attachments
- Screenshot: ![BUG-004](./assets/BUG-004/bug-004.png)
- Console: [`console.txt`](./assets/BUG-004/console.txt)

---

## 🔗 Related Tests
- `LOGIN-001–012` (Login Feature suite) — add a case to verify **Forgot password** link routes to reset.

---

## 🗒️ Notes
- When server endpoints exist, add coverage for reset email request & token flow (happy/invalid token/expired).
