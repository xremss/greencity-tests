## Test Case 1: Successful Sign Up

**Preconditions:**
- User with the given email is not registered
- Sign Up popup is opened

**Test Steps:**

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Enter email in the Email field | test@gmail.com | — |
| 2 | Enter Username | testuser | — |
| 3 | Enter password in the Password field | 12345678Qw! | — |
| 4 | Enter password in Confirm Password field | 12345678Qw! | — |
| 5 | Click Sign Up button | — | Popup is closed and user sees a successful registration message |

---

## Test Case 2: Reset Password

**Preconditions:**
- Account with a valid email is already registered

**Test Steps:**

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click Forgot Password button | — | Password reset form is displayed |
| 2 | Enter email | test@gmail.com | — |
| 3 | Click "Submit a login link" button | — | Password reset email is sent |
| 4 | Open the link from the email | — | User is redirected to the password reset page |
| 5 | Enter new password | 12345678Qw! | — |
| 6 | Enter Confirm Password | 12345678Qw! | — |
| 7 | Click Change Password button | — | User sees a successful password change message |

---

## Test Case 3: Sign In with Invalid Credentials

**Preconditions:**
- Account is registered

**Test Steps:**

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click Sign In button | — | Sign In form is displayed |
| 2 | Enter email | test@gmail.com | — |
| 3 | Enter incorrect password | wrongPassword123 | Input is accepted |
| 4 | Click Sign In button | — | Error message "Bad email or password" is displayed |