# Test Case — LOGIN-020 — Lockout Window Automatically Lifts

**ID:** LOGIN-020  
**Module:** Authentication → Login/Lockout  
**Owner:** Walter Lam  
**Priority:** P1  
**Preconditions:** Account is locked due to prior failed attempts; lockout window (e.g., 15 min) is known.

## Steps
1. Wait until the lockout window has elapsed.
2. Attempt to log in with **correct** credentials.

## Expected Result
- Lockout state **clears** after the window.  
- Login succeeds; prior lockout banner is gone.  
- Audit log shows lockout release.

## Actual Result
_TBD_

## Status
☐ Pass  ☐ Fail  ☐ Blocked
