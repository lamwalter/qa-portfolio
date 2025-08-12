# 🐞 Bug Report: Add to Cart Appears to Work, But Cart is Empty

**Bug ID:** BUG-002  
**Reported by:** Walter Lam  
**Date:** August 6, 2025  
**Severity:** Medium  
**Priority:** P2  

---

## 🧩 Summary
When clicking "Add to Cart" on a product page, the UI responds normally, but the shopping cart remains empty when accessed.

---

## 🔁 Steps to Reproduce
1. Go to `https://example.com/products/blue-jacket`
2. Click the **Add to Cart** button
3. Navigate to the **Cart** page via the top navigation or `/cart`

---

## ✅ Expected Result
The selected product should appear in the shopping cart with quantity = 1.

---

## ❌ Actual Result
The cart page is empty. No items are displayed.

---

## 🌐 Environment
- **OS:** macOS Ventura 13.5  
- **Browser:** Safari 17.0  
- **Device:** MacBook Air (M2, 2022)

---

## 🛠️ Technical Details
- **Console Warning:**  
  `POST /cart/add → 200 OK (no payload returned)`
- **Storage Check:**  
  `localStorage.cart` shows `[]` (empty array)

---

## 📎 Attachments
- Screenshot: `bug-002.png`

---

## 📌 Notes
Likely caused by missing backend session sync or failure to update cart state in local storage.
