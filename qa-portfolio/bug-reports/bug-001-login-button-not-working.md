# Bug Report: Login Button Not Working

## Bug ID: BUG-001

### Summary:
Clicking the login button on the homepage does nothing after entering valid credentials.

### Steps to Reproduce:
1. Go to `https://example.com`
2. Enter a valid email and password
3. Click the **Login** button

### Expected Result:
User should be redirected to the dashboard after successful login.

### Actual Result:
Nothing happens. No error message is displayed. No redirect occurs.

### Environment:
- OS: Windows 11
- Browser: Chrome 115.0.5790.171 (64-bit)
- Device: Desktop

### Severity: High  
### Priority: P1

### Attachments:
- Screenshot: `bug-001.png`
- Console Log Error:  
  `Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')`

### Notes:
May be caused by incorrect binding of the click event listener or JS not loading properly.

### Reported by: Walter Lam  
### Date: August 5, 2025
