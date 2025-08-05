### 🐞 Bug Report

**Title**: App crashes when deleting past-due task

**Environment**:
- Device: Desktop
- OS: Windows 10
- Browser: Chrome 115
- App Version: v1.4.0

**Severity**: High  
**Priority**: P1

**Steps to Reproduce**:
1. Open the Todo List App.
2. Create a task with a due date of yesterday.
3. Click "Delete" on the task.

**Expected Result**:
Task is removed from the list without any issues.

**Actual Result**:
The app crashes and shows a blank screen.

**Screenshot / Video**:  
*(Insert if available)*

**Console Logs**:
```bash
TypeError: Cannot read properties of undefined (reading 'id')
    at deleteTask (TaskManager.js:102)

**Suggested Fix**:  
Add null check for task ID before attempting to delete.

**Jira Reference**:  
[CRM-13 – App crashes when deleting past-due task](https://walterqa.atlassian.net/browse/CRM-13)
