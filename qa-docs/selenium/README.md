# Selenium IDE — Login Smoke

**Demo site:** SauceDemo → `https://www.saucedemo.com`

**Files in this folder**
- **Suite:** [`login-smoke.side`](./login-smoke.side)
- **Screens:** [`assets/login-page.png`](./assets/login-page.png), [`assets/login-success.png`](./assets/login-success.png), [`assets/login-error.png`](./assets/login-error.png)

## Prereqs (GUI)
- Firefox + **Selenium IDE** add-on (recommended).  
  *Chrome note:* the original IDE extension is deprecated on Chrome; Firefox IDE works reliably.

## How to run (GUI / Firefox)
1) Open **Selenium IDE** → **File ▸ Open** → select `qa-docs/selenium/login-smoke.side`.
2) Set **Project base URL** to `https://www.saucedemo.com`.
3) In the top-left, open the **▼** dropdown next to the run button and choose **“login-smoke”** (the test suite).
4) Click **Run** (▶).  
   - **SEL-001**: logs in with valid creds and lands on the **Products** page.  
   - **SEL-002**: logs in with invalid password and shows the red **“Epic sadface…”** error.

### Capturing screenshots (for the repo)
- `assets/login-page.png` – before login (form visible).
- `assets/login-success.png` – after valid login (inventory list visible).
- `assets/login-error.png` – after invalid login (red error banner visible).

> Tip (Windows): **Win+Shift+S** → Rectangle snip → Save.  
> Tip (Mac): **⌘+Shift+4**.

## Locators (cheat sheet)
- Username: `id=user-name`  
- Password: `id=password`  
- Login button: `id=login-button`  
- Success marker: `css=.inventory_list`  
- Error message: `css=h3[data-test="error"]`

## Troubleshooting
- **Blank window** after clicking *Test Suites*: close the IDE window and reopen the `.side` file.
- **“Unknown file was received”**: ensure the file extension is exactly `.side` (not downloaded as `.json`).
- Flaky timing? Increase waits or replace `assert*` with `verify*` on non-critical checks.

## Links
- **Run summary:** [`Selenium IDE — Login Smoke`](../../test-summaries/selenium-ide-login-smoke.md)
- **Portfolio map:** [`Root README`](../../README.md)

---

## (Optional) Run from terminal
> CLI is optional; IDE GUI is enough for this portfolio.

You’ll need Node.js and Firefox. Then:
```bash
# one of these may work depending on your npm registry
npx @seleniumhq/side-runner -c "browserName=firefox" qa-docs/selenium/login-smoke.side
# or
npx selenium-side-runner -c "browserName=firefox" qa-docs/selenium/login-smoke.side
