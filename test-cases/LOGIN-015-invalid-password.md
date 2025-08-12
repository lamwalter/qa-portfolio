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

git commit -m "CRM-11 invalid_password_test_case.md"

# Test Case: Invalid Password Handling

**Test ID:** TC-003  
**Feature:** Login Error Handling  
**Priority:** Medium  

## Preconditions:
- User has valid Gmail account
- Browser is open

## Steps:
1. Navigate to https://mail.google.com
2. Enter valid email address
3. Enter invalid password
4. Click "Login"

## Expected Result:
- Error message displayed: "Wrong password. Try again."

## Actual Result:
- TBD

## Status:
- Pass / Fail
