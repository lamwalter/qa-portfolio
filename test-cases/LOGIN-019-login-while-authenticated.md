# Test Case — LOGIN-019 — Visit /login While Already Authenticated

**ID:** LOGIN-019  
**Module:** Authentication → Login/Routing  
**Owner:** Walter Lam  
**Priority:** P3  
**Preconditions:** User is logged in.

## Steps
1. While authenticated, navigate directly to `/login`.

## Expected Result
- User is **redirected** to the default authenticated page (e.g., `/dashboard`).  
- No flicker or double-render of the login form.

## Actual Result
_TBD_

## Status
☐ Pass  ☐ Fail  ☐ Blocked
