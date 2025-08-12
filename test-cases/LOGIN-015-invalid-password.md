# Test Case — LOGIN-015 — Invalid Password Handling

**Module:** Authentication → Login  
**Owner:** Walter Lam  
**Priority:** P1  
**Preconditions:** Existing active user account.

## Steps
1. Go to `/login`.
2. Enter a valid email and an **incorrect** password.
3. Click **Login**.

## Test Data
- Email: `valid.user@example.com`
- Password: `WrongPass!234`

## Expected Result
- User is **not** logged in; remains on login page.
- Clear error message shown (e.g., “Email or password is incorrect.”) without revealing which field was wrong.
- No session/cookies created; rate limiter increments failed-attempt counter.
- No stack traces in UI/console; no sensitive info in responses.
- (If lockout policy exists) failed-attempts count increases toward threshold.

## Actual Result
_TBD_

## Status
☐ Pass ☐ Fail ☐ Blocked

## Notes / Links
- Related bugs: consider linking to BUG-001 if messaging/redirect issues reoccur.

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
