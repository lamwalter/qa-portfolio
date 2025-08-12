# Test Summary Report – <Feature / Release / Sprint>

**Project/App:** <name>  
**Scope / Feature:** <e.g., Authentication – Login>  
**Build / Version:** <e.g., 1.4.0-rc.3>  
**Test Window:** <start → end dates>  
**Tester(s):** Walter Lam  
**Environment:** OS <…>, Browser <…>, Device <…>  
**Related Artifacts:** Test Plan • Test Cases folder • Bug Reports folder

---

## 1) Execution Summary
| Metric | Count |
|---|---:|
| Test cases planned | <#> |
| Executed | <#> |
| **Passed** | <#> |
| **Failed** | <#> |
| **Blocked/Not run** | <#> |

**Pass Rate** = `Passed / Executed × 100%` → **<xx>%**  
**Overall Result:** ✅ Accept / ⚠️ Accept with risks / ❌ Reject

---

## 2) Coverage
- Areas covered: <modules, platforms, browsers>  
- Out of scope: <anything not tested>  
- Data sets used: <brief note if relevant>

---

## 3) Defects Found (link to bug files)
| ID | Title | Sev | Pri | Status | Link |
|---|---|---|---|---|---|
| BUG-001 | Login button not working | High | P1 | Open | `bug-reports/bug-001-login-button-not-working.md` |
| BUG-002 | Add to cart success but cart empty | Medium | P2 | Open | `bug-reports/bug-002-add-to-cart-empty-cart.md` |
<!-- Add rows as needed -->

**Notes:** Group similar issues; highlight any blockers.

---

## 4) Notable Findings & Risks
- <e.g., Rate limiter missing on login; risk of brute force>
- <e.g., Inconsistent validation messages across browsers>

**Impact:** <user impact / business impact>  
**Likelihood:** Low / Medium / High  
**Mitigation / Next action:** <owner + plan>

---

## 5) Recommendations
- Fix high-sev defects before release (list IDs)  
- Re-run regression on <areas>  
- Add new test cases for <gaps discovered>

---

## 6) Sign-off
| Role | Name | Decision | Date |
|---|---|---|---|
| QA | Walter Lam | ✅ / ⚠️ / ❌ | <date> |
| Dev Lead | <name> | ✅ / ⚠️ / ❌ | <date> |
| PM/Owner | <name> | ✅ / ⚠️ / ❌ | <date> |

---

## Appendix (optional)
- Execution log / screenshots  
- Traceability: map of Test Case IDs → Requirements/Stories
