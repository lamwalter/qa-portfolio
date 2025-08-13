# Test Case — LOGIN-017 — Allowed Special Characters in Password

**ID:** LOGIN-017  
**Module:** Authentication → Login  
**Owner:** Walter Lam  
**Priority:** P2  
**Preconditions:** Password policy allows common special characters.

## Steps
1. Log in with a password containing many special characters:  
   `!@#$%^&*()_+-=[]{}|;':",.<>/?\`~`
2. (If policy allows) include extended characters (e.g., `ñ`, `é`) and retry with valid creds.

## Expected Result
- With correct credentials, login **succeeds**.  
- Allowed characters are accepted; no improper sanitization.  
- No XSS/HTML injection via rendered messages.

## Actual Result
_TBD_

## Status
☐ Pass  ☐ Fail  ☐ Blocked
