# Test Suite — LOGIN-001…012 — Login Feature

**Module:** Authentication → Login  
**Owner:** Walter Lam  
**Last Updated:** 2025-08-11  
**Scope:** Positive login • Negative inputs • Security/abuse • UX/behavior • Session & Logout • Forgot Password link

## Contents
- [LOGIN-001 — Successful login with valid credentials](#tc-id-login-001--successful-login-with-valid-credentials)
- [LOGIN-002 — Empty email and password](#tc-id-login-002--empty-email-and-password)
- [LOGIN-003 — Invalid email format](#tc-id-login-003--invalid-email-format)
- [LOGIN-004 — Wrong password for valid email](#tc-id-login-004--wrong-password-for-valid-email)
- [LOGIN-005 — Leading/trailing whitespace trimmed](#tc-id-login-005--leadingtrailing-whitespace-trimmed)
- [LOGIN-006 — Case sensitivity rules](#tc-id-login-006--case-sensitivity-rules)
- [LOGIN-007 — Remember me persists session](#tc-id-login-007--remember-me-persists-session)
- [LOGIN-008 — Account lockout after N failed attempts](#tc-id-login-008--account-lockout-after-n-failed-attempts)
- [LOGIN-009 — SQL injection attempt in email](#tc-id-login-009--sql-injection-attempt-in-email)
- [LOGIN-010 — XSS attempt in email](#tc-id-login-010--xss-attempt-in-email)
- [LOGIN-011 — Session persists on refresh](#tc-id-login-011--session-persists-on-refresh)
- [LOGIN-012 — Logout clears session](#tc-id-login-012--logout-clears-session)

---

### TC ID: LOGIN-001 — Successful login with valid credentials
**Preconditions**: User account exists and is active.  
**Steps**
1. Go to `/login`.
2. Enter valid email and password.
3. Click **Login**.  
**Data**: `valid.user@example.com` / `ValidPass!234`  
**Expected**
- Redirect to `/dashboard`; user avatar/name visible.
- Session cookie set (HttpOnly, Secure); CSRF present if applicable.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked  **Notes:** —

---

### TC ID: LOGIN-002 — Empty email and password
**Steps**
1. Go to `/login`, leave both fields empty.
2. Click **Login**.  
**Expected**
- Inline validation for both fields (e.g., “Email is required”, “Password is required”).
- No request sent to server.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-003 — Invalid email format
**Data**: Email `abc@no_tld`, any password.  
**Expected**
- Client-side email format validation error.
- No server call.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-004 — Wrong password for valid email
**Data**: `valid.user@example.com` / `WrongPass!234`  
**Expected**
- Error: “Email or password is incorrect.”
- No session created; rate limiter increments.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked  **Notes:** Link BUG if message missing.

---

### TC ID: LOGIN-005 — Leading/trailing whitespace trimmed
**Data**: Email/Password wrapped in spaces.  
**Expected**
- Whitespace trimmed; login should succeed if creds valid.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-006 — Case sensitivity rules
**Data**: Email case-variant, correct password case.  
**Expected**
- Email comparison case-insensitive (per spec); password case-sensitive.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-007 — Remember me persists session
**Steps**
1. Check **Remember me** and log in.
2. Close browser; reopen and visit site.  
**Expected**
- Still logged in (per configured max-age); persistent cookie has correct flags.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-008 — Account lockout after N failed attempts
**Preconditions**: Lockout threshold configured (e.g., 5/15min).  
**Steps**
1. Enter wrong password repeatedly to threshold +1.  
**Expected**
- Account locked; clear message shown; attempts denied during lockout window.
- Optional email notification sent.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-009 — SQL injection attempt in email
**Data**: `test@example.com' OR '1'='1` / `x`  
**Expected**
- Validation rejects; no SQL errors or unintended access.
- No stack traces.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-010 — XSS attempt in email
**Data**: `<script>alert(1)</script>@x.com` / `x`  
**Expected**
- Input sanitized; no script execution; normal error shown.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-011 — Session persists on refresh
**Preconditions**: Logged in.  
**Steps**: Refresh page; open protected route.  
**Expected**
- Session remains valid; no re-login prompt.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-012 — Logout clears session
**Preconditions**: Logged in.  
**Steps**: Click **Logout** → visit `/dashboard`.  
**Expected**
- Redirected to `/login`; session/refresh tokens cleared; cookies removed.  
**Actual:** _TBD_  **Status:** ☐ Pass ☐ Fail ☐ Blocked
