# Test Case — LOGIN-013 — Gmail OAuth Login

**Module:** Authentication → Login (OAuth)  
**Owner:** Walter Lam  
**Priority:** P2  
**Preconditions:** Google account available; OAuth client configured.

## Steps
1. Click **Login with Google**.
2. Select a valid Google account.
3. Approve consent if prompted.

## Test Data
- Google account: `test.user@gmail.com`

## Expected Result
- User is redirected back and logged in.
- Session cookie set; profile shows Google-linked email.

## Actual Result
_TBD_

## Status
☐ Pass ☐ Fail ☐ Blocked

## Notes / Links
- Related bugs: —

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
