# Test Case — LOGIN-014 — YouTube OAuth Login

**Module:** Authentication → Login (OAuth)  
**Owner:** Walter Lam  
**Priority:** P2  
**Preconditions:** YouTube/Google account available; OAuth client configured with correct redirect URI.

## Steps
1. On `/login`, click **Continue with YouTube**.
2. In the Google/YouTube consent screen, select a valid account.
3. Approve requested permissions (if prompted).
4. Complete the redirect back to the application.

## Test Data
- Google/YouTube account: `test.user@gmail.com`

## Expected Result
- App receives authorization code → exchanges for access token.
- User is logged in and redirected to `/dashboard`.
- Profile shows `YouTube/Google`-linked identity (email or name).
- Session cookie set (HttpOnly, Secure); CSRF token present as applicable.
- No stack traces or OAuth errors in console/network.

## Actual Result
_TBD_

## Status
☐ Pass ☐ Fail ☐ Blocked

## Notes / Links
- Related bugs: —
- Network: Verify 302 to OAuth provider and 200 on callback route.

git commit -m "CRM-12 youtube_login_test_case.md"

# Test Case: YouTube Login Functionality

**Test ID:** TC-002  
**Feature:** User Authentication  
**Priority:** High  

## Preconditions:
- User has valid Google account
- Browser is open

## Steps:
1. Navigate to https://www.youtube.com
2. Click "Sign In"
3. Enter valid email & password
4. Click "Next"

## Expected Result:
- User is redirected to YouTube homepage logged in

## Actual Result:
- TBD

## Status:
- Pass / Fail
