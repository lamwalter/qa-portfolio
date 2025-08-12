# Test Summary Report – Login Cycle 01 (Aug 2025)

**Project/App:** <name>  
**Scope / Feature:** Authentication – Login (Core + OAuth)  
**Build / Version:** <e.g., 1.4.0-rc.3>  
**Test Window:** <YYYY-MM-DD> → <YYYY-MM-DD>  
**Tester(s):** Walter Lam  
**Environment:** OS <…>, Browser <…>, Device <…>  

**Related Artifacts:**  
- Test Plan: `manual-qa/test-plan-template.md`  
- Test Cases (suite): `test-cases/LOGIN-001-012-login-feature-suite.md`  
- Test Cases (singles): `test-cases/LOGIN-013-gmail-oauth.md`, `LOGIN-014-youtube-oauth.md`, `LOGIN-015-invalid-password.md`  
- Bug Reports: `bug-reports/`

---

## 1) Execution Summary
| Metric | Count |
|---|---:|
| Test cases planned | 15 |
| Executed | 0 |
| **Passed** | 0 |
| **Failed** | 0 |
| **Blocked/Not run** | 0 |

**Pass Rate** = `Passed / Executed × 100%` → **0%**  
**Overall Result:** ☐ ✅ Accept ☐ ⚠️ Accept with risks ☐ ❌ Reject

---

## 2) Coverage
- **Covered:** Core login, validation, session/remember-me, logout, lockout, OAuth (Google/YouTube).  
- **Out of scope:** Password reset flow beyond link presence; MFA.  
- **Data sets:** Valid user, invalid password variants, OAuth sandbox account(s).

---

## 3) Defects Found
| ID | Title | Sev | Pri | Status | Link |
|---|---|---|---|---|---|
| BUG-001 | Login button not working | High | P1 | Open | `bug-reports/bug-001-login-button-not-working.md` |
| BUG-002 | Add to cart appears successful but cart is empty | Medium | P2 | Open | `bug-reports/bug-002-add-to-cart-empty-cart.md` |

**Notes:** Update table as you test; add new rows for fresh defects.

---

## 4) Notable Findings & Risks
- <e.g., Rate limiter absent on login; brute-force risk>  
- <e.g., Inconsistent validation messages across browsers>

**Impact:** <user/business impact>  
**Likelihood:** Low / Medium / High  
**Mitigation / Next action:** <owner + plan>

---

## 5) Recommendations
- Fix High/P1 defects before release: <IDs>  
- Re-run regression on login/logout + session persistence  
- Add test cases for <gaps discovered>

---

## 6) Sign-off
| Role | Name | Decision | Date |
|---|---|---|---|
| QA | Walter Lam | ☐ ✅ / ☐ ⚠️ / ☐ ❌ | <date> |
| Dev Lead | <name> | ☐ ✅ / ☐ ⚠️ / ☐ ❌ | <date> |
| PM/Owner | <name> | ☐ ✅ / ☐ ⚠️ / ☐ ❌ | <date> |

---

## Appendix (optional)
- Execution log / screenshots  
- Traceability: Test Case IDs → Requirements/Stories
