# Selenium IDE — Login Smoke

Quick UI smoke for the SauceDemo site.

**Demo site:** SauceDemo → `{{baseUrl}}` = https://www.saucedemo.com

---

## Files in this folder

- **Suite:** [`login-smoke.side`](./login-smoke.side)
- **Screens (PNG):** [`assets/`](./assets/)
  - `login-page.png`  – before login
  - `login-success.png` – after valid login
  - `login-error.png`   – after invalid password
- (This README)

---

## Tests

**SEL-001 – Login success (valid creds)**  
Asserts we land on the inventory page.

- open `/`
- type `id=user-name` → `standard_user`
- type `id=password` → `secret_sauce`
- click `id=login-button`
- waitForElementVisible `css=.inventory_list` (5000)
- assertText `css=span.title` → `Products`

**SEL-002 – Login error (bad password)**  
Asserts the red error banner is shown.

- open `/`
- type `id=user-name` → `standard_user`
- type `id=password` → `wrongpass`
- click `id=login-button`
- waitForElementVisible `css=[data-test="error"]` (5000)
- assertText `css=[data-test="error"]` →  
  `Epic sadface: Username and password do not match any user in this service`

---

## How to run (Firefox)

> Chrome has removed the IDE from the Web Store; Firefox still supports it.

1) Install **Selenium IDE** (Firefox Add-ons).  
2) Open the IDE → **File ▸ Open project…** → select `login-smoke.side`.  
3) Set **Playback base URL** (top bar) → `https://www.saucedemo.com`.  
4) Left sidebar: click **Test Suites** (stack icon) → select **Smoke** → ▶ Run.  
   - Or run a single test by selecting it in **Tests** and pressing ▶.

---

## Screenshots for the repo

Take these three and save them into `qa-docs/selenium/assets/`:

- `login-page.png` – fresh login page
- `login-success.png` – inventory page visible
- `login-error.png` – red banner after bad password

Tips:
- **Windows:** `Win` + `Shift` + `S` → Rectangle snip → Save.  
- **macOS:** `Cmd` + `Shift` + `4` → Drag → Save.  
- Selenium IDE’s `saveScreenshot` (if used) saves to your **Downloads** folder; rename/move into `qa-docs/selenium/assets/` with the filenames above.

---

## Locators (cheat sheet)

- Username: `id=user-name`  
- Password: `id=password`  
- Login button: `id=login-button`  
- Success marker: `css=.inventory_list` (list present)  
- Title text: `css=span.title` → `Products`  
- Error banner: `css=[data-test="error"]`

---

## Notes / Troubleshooting

- Valid demo creds: **`standard_user` / `secret_sauce`**.  
- If a `waitForElementVisible` step flakes, bump timeout to **5000–8000 ms**.  
- If `assertText` is picky (whitespace/case), switch to **`verifyText`** or assert a stable **CSS** exists (`.inventory_list`).  
- If the IDE ever opens blank or “Test Suites” view hangs, close the IDE window and reopen (`Tools ▸ Selenium IDE`).  
- If opening the project shows “Unknown file was received”, make sure you use **File ▸ Open project…** on the `.side` file (don’t drag-drop a web link).

---

## Commit suggestions

- Initial suite: `Selenium: add IDE login smoke (README + .side)`  
- After PNGs: `Selenium: add screenshots (login page/success/error)`
