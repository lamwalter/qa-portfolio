# Test Cases — Login Feature

**Module:** Authentication → Login  
**Owner:** Walter Lam  
**Last Updated:** 2025-08-11

## Coverage Map
- ✅ Positive login
- ⚠️ Negative inputs (empty, invalid email, wrong password)
- 🔐 Security/Abuse (lockout, injection, XSS)
- 🧠 UX/Behavior (remember me, trimming, case)
- 🔁 Session & logout
- 🔗 Navigation (Forgot Password)

---

### TC ID: LOGIN-001 — Successful login with valid credentials
**Preconditions**
- User account exists and is active.

**Steps**
1. Go to `/login`.
2. Enter valid email and password.
3. Click **Login**.

**Data**
- Email: `valid.user@example.com`
- Password: `ValidPass!234`

**Expected**
- Redirect to `/dashboard`.
- User avatar/name visible.
- Session cookie set (HttpOnly, Secure).

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked  
**Notes/Links:** Related bugs: —

---

### TC ID: LOGIN-002 — Empty email and password
**Steps**
1. Go to `/login`.
2. Leave both fields empty.
3. Click **Login**.

**Expected**
- Inline validation for both fields (e.g., “Email is required”, “Password is required”).
- No request sent to server.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-003 — Invalid email format
**Data**
- Email: `abc@no_tld`
- Password: `anything`

**Expected**
- Client-side validation error for email format.
- No server call.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-004 — Wrong password for valid email
**Data**
- Email: `valid.user@example.com`
- Password: `WrongPass!234`

**Expected**
- Error: “Email or password is incorrect.”
- No login session created.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked  
**Notes:** Link BUG if message missing.

---

### TC ID: LOGIN-005 — Leading/trailing whitespace trimmed
**Data**
- Email: `  valid.user@example.com  `
- Password: `  ValidPass!234  `

**Expected**
- Whitespace trimmed; login succeeds.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-006 — Case sensitivity rules
**Data**
- Email: `VALID.USER@example.com` (case variant)
- Password: correct case

**Expected**
- Email comparison is case-insensitive; login succeeds (per spec).
- Password is case-sensitive.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-007 — Remember me persists session
**Steps**
1. Check **Remember me**.
2. Login successfully.
3. Close browser; reopen and visit site.

**Expected**
- User remains logged in (per configured max-age).
- Persistent cookie set; security flags correct.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-008 — Account lockout after N failed attempts
**Preconditions**
- Lockout threshold configured (e.g., 5 attempts / 15 min).

**Steps**
1. Enter wrong password repeatedly until threshold +1.

**Expected**
- Account locked; clear message shown.
- Further attempts denied during lockout window.
- Email notification sent (optional).

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-009 — SQL injection attempt in email
**Data**
- Email: `test@example.com' OR '1'='1`
- Password: `x`

**Expected**
- Validation error; no server error/stack trace.
- No injection executed.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-010 — XSS attempt in email
**Data**
- Email: `<script>alert(1)</script>@x.com`
- Password: `x`

**Expected**
- Input sanitized; no script execution.
- Error shown normally.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-011 — Session persists on refresh
**Preconditions**
- Logged in.

**Steps**
1. Refresh page.
2. Navigate to a protected page.

**Expected**
- Session remains valid; no relogin prompt.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked

---

### TC ID: LOGIN-012 — Logout clears session
**Preconditions**
- Logged in.

**Steps**
1. Click **Logout**.
2. Visit a protected route (e.g., `/dashboard`).

**Expected**
- Redirect to `/login`.
- Session/refresh token cleared; cookies removed.

**Actual:** _TBD_  
**Status:** ☐ Pass ☐ Fail ☐ Blocked
