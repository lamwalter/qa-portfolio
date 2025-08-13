# Test Case — LOGIN-016 — Password Length Boundaries

**ID:** LOGIN-016  
**Module:** Authentication → Login  
**Owner:** Walter Lam  
**Priority:** P2  
**Preconditions:** Password policy defines min/max length (e.g., 8–64).

## Steps
1. Attempt login with a valid email and a password **shorter** than minimum (e.g., 5 chars).
2. Attempt login with a password exactly at **minimum** (e.g., 8 chars) using valid creds.
3. Attempt login with a password exactly at **maximum** (e.g., 64 chars) using valid creds.
4. Attempt login with a password **longer than maximum** (e.g., 65+).

## Data
- Same valid email; vary password lengths as above.

## Expected Result
- Too short / too long → validation or clear server error; **no login**.
- At min/max boundary with correct creds → **login succeeds**.
- Messages are consistent; no stack traces.

## Actual Result
_TBD_

## Status
☐ Pass  ☐ Fail  ☐ Blocked
