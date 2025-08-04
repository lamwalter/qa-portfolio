
#### 🔧 Action:
📁 Save this as `bug_report_001.md` in your GitHub repo under `/qa-docs/bug-reports`.

---

### ✅ **2. Start Manual Test Plan Doc in GitHub**

Here’s a minimal starting template:

```markdown
# 🧪 Manual Test Plan – Todo List Web App

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
- [ ] Delete normal task
- [ ] Delete overdue task
- [ ] Cancel deletion

## 🧩 Edge Cases
- [ ] Task with emoji/title in different language
- [ ] Task created and deleted in under 2 seconds

## 👁️ UI Checks
- [ ] Responsive design on mobile
- [ ] Button states (disabled/enabled, hover)

---

### 🛠️ Tools
- Chrome Dev Tools
- Postman (for API endpoints)
