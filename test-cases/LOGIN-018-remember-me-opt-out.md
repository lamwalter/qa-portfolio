# Test Case — LOGIN-018 — Remember Me Opt-Out (Session-Only)

**ID:** LOGIN-018  
**Module:** Authentication → Login  
**Owner:** Walter Lam  
**Priority:** P2  
**Preconditions:** App supports “Remember me”.

## Steps
1. Leave **“Remember me” unchecked**.
2. Log in with valid credentials.
3. Close the browser completely; reopen and navigate to a protected route.

## Expected Result
- User is **logged out** (session-only).  
- No persistent auth cookie remains (check cookie expiry/flags).

## Actual Result
_TBD_

## Status
☐ Pass  ☐ Fail  ☐ Blocked
