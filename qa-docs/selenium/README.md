# Selenium IDE — Login Smoke

**Demo site:** SauceDemo → `{{baseUrl}} = https://www.saucedemo.com`

## Tests
- **SEL-001** Login success (valid creds) → lands on inventory page
- **SEL-002** Login error (bad password) → shows “Epic sadface …” error

## How to run (Chrome/Firefox)
1) Install **Selenium IDE** extension.
2) **File → Open** → import `login-smoke.side`.
3) Ensure **Project base URL** is `https://www.saucedemo.com`.
4) Run **Suite: Smoke** (or run tests individually).

## Screenshots for repo
Grab and save as:
- `qa-docs/selenium/assets/login-page.png` (before login)
- `qa-docs/selenium/assets/login-success.png` (after valid login)
- `qa-docs/selenium/assets/login-error.png` (after invalid password)

> Tip (Windows): `Win + Shift + S` → Rectangle snip → Save.  
> Tip (Mac): `Cmd + Shift + 4`.

## Locators (cheat sheet)
- Username: `id=user-name`  
- Password: `id=password`  
- Login button: `id=login-button`  
- Success page marker: `css=.inventory_list`  
- Error message: `css=h3[data-test='error']`

## Notes
- Valid demo creds: `standard_user / secret_sauce`
- If Selenium IDE warns on an assertion, swap **assert** ↔ **verify**.
