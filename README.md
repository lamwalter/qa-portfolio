# qa-portfolio

Manual QA portfolio: **test plans, test cases, and bug reports** stored in GitHub for easy review.

---

## 📂 Portfolio Map
- 🐛 **Bug Reports:** [`./bug-reports/`](./bug-reports/)
  - [BUG-001 – Login button not working](./bug-reports/bug-001-login-button-not-working.md)
  - [BUG-002 – Add to cart appears successful but cart is empty](./bug-reports/bug-002-add-to-cart-empty-cart.md)
- ✅ **Test Cases:** [`./test-cases/`](./test-cases/)
- 📘 **Manual QA Docs:** [`./manual-qa/`](./manual-qa/)
  - [Test Plan Template](./manual-qa/test-plan-template.md)
- 🧾 **QA Docs / Checklists:** [`./qa-docs/`](./qa-docs/)

---

## 🔄 Testing Workflow (Manual)
1. Write **test cases** in Markdown and save to `test-cases/`.
2. Execute tests; update each case with **Actual Result** and **Status** (Pass/Fail/Blocked).
3. Log defects as **Bug Reports** in `bug-reports/` with clear steps, expected vs actual, and environment.
4. Link related items inside files (e.g., “Related: BUG-001” or “Covers: LOGIN-001”).
5. Summarize results in a **Test Summary** doc (per feature or sprint) under `qa-docs/`.

---

## 🐛 Bug Report Conventions
- **Filename:** `bug-###-short-title.md` (e.g., `bug-002-add-to-cart-empty-cart.md`)
- **Fields:** Summary • Steps to Reproduce • Expected • Actual • Environment • Severity • Priority • Attachments • Notes
- **Severity:** Blocker > Critical > **High** > Medium > Low  
- **Priority:** **P1** (urgent) > P2 > P3

---

## ✅ Test Case Conventions
- **ID:** `FEATURE-###` (e.g., `LOGIN-001`)
- **Fields:** Title • Preconditions • Steps • Expected • Actual • Status • Notes
- Keep steps **atomic** (one action per step) and expected results **observable**.

---

## 📊 Progress (QA Portfolio)
- Test Plan: **✅** (template committed)
- Bug Reports: **2 / 10** (target) — **🟡 in progress**
- Test Cases: **0 / 12** (target) — **🟠 starting next**
- Test Summary Docs: **0 / 3** — **🔴 pending**

---

## 📁 Folder Structure
qa-portfolio/
bug-reports/ — Individual defect reports (Markdown)

manual-qa/ — Plans, workflows, SOPs

qa-docs/ — Checklists, summaries, templates

test-cases/ — Manual test cases
