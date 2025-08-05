# 🧪 Manual Test Plan – Todo List Web App

## 🔗 Jira References
- Test Case: [CRM-14 – Task Deletion Test Case](https://walterqa.atlassian.net/browse/CRM-14)
- Bug Report: [CRM-13 – Past-due task crash](https://walterqa.atlassian.net/browse/CRM-13)

## 📦 Scope
Manual test plan for functional, usability, and UI testing.

## ✅ Test Scenarios

### 🔹 Task Creation
- [ ] Create task with valid input
- [ ] Create task with empty title (should fail)
- [ ] Create task with long description (> 500 chars)

### 🔹 Task Editing
- [ ] Edit title and save
- [ ] Cancel during edit (changes not saved)

### 🔹 Task Deletion
- [ ] Delete normal task – [CRM-14](https://walterqa.atlassian.net/browse/CRM-14)
- [ ] Delete overdue task
- [ ] Cancel deletion

## 🧩 Edge Cases
- [ ] Task with emoji/title in different language
- [ ] Task created and deleted in under 2 seconds

## 👁️ UI Checks
- [ ] Responsive design on mobile
- [ ] Button states (disabled/enabled, hover)

## 🛠️ Tools
- Chrome Dev Tools
- Postman (for API endpoints)
