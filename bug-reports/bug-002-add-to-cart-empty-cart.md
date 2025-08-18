# 🐞 Bug Report: Add to Cart Appears to Work, But Cart is Empty

**Bug ID:** BUG-002  
**Reported by:** Walter Lam  
**Date:** August 6, 2025  
**Severity:** Medium  
**Priority:** P2  

---

## 🧩 Summary
When clicking "Add to Cart" on a product page, the UI responds normally, but the shopping cart remains empty when accessed.
Issue persists after hard refresh and across navigation.

---

## 🔁 Steps to Reproduce
1. Go to `https://example.com/products/blue-jacket`
2. Click the **Add to Cart** button
3. Navigate to the **Cart** page via top navigation or go to /cart.

---

## ✅ Expected Result
Selected product appears in cart with quantity = 1 and correct name/price.

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
- No Set-Cookie/session update observed on add; localStorage.cart remains [].

---

## 📎 Attachments
- Screenshot: ![BUG-002](./assets/BUG-002/bug-002.png)

---

## 📌 Notes
Likely caused by missing backend session sync or failure to update cart state in local storage.
Likely missing server-side session write or cart merge from local storage.
