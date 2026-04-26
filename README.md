# GreenCity Test Automation

Automated UI test suite for the GreenCity web application using Selenium, Pytest, and Allure reporting.

## Overview

This project contains automated test cases for the following features:
- **Sign Up** - User registration functionality
- **Sign In** - User login with invalid credentials
- **Reset Password** - Password reset functionality

## Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Git

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd greencity-tests
```

### 2. Create Virtual Environment

```powershell
# Windows
python -m venv greencity

# Activate virtual environment
.\greencity\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### Environment Variables

1. Copy the example file:

```bash
cp data/.env.example data/.env
```

2. Edit `data/.env` and fill in your actual values:
See `data/.env.example` for all available configuration options.

## Running Tests

### Run All Tests

```bash
# Clear previous results and run tests
pytest --alluredir=allure-results
```

### Run Specific Test File

```bash
pytest tests/sign-up-TC.py -v
pytest tests/Sign-In-Invalid-Credentials-TC3.py -v
pytest tests/reset-password-TC2.py -v
```

### Run Tests with Verbose Output

```bash
pytest tests/ -v --tb=short
```

## Viewing Test Reports

### Generate and View Allure Report

```bash
# Install Allure (if not already installed)
# For Windows with Scoop: scoop install allure
# For Windows with Chocolatey: choco install allure

# Generate and open Allure report
allure serve allure-results
```

This will open an interactive HTML report showing:
- Test execution history
- Test details with steps
- Screenshots (if captured)
- Test duration
- Pass/Fail status

## Project Structure

```
greencity-tests/
├── data/
│   ├── .env                 # Environment variables (gitignored)
│   ├── .env.example         # Example environment configuration
│   └── config.py            # Configuration class
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── base_component.py
│   │   ├── signin_modal.py
│   │   ├── signup_modal.py
│   │   └── reset_password_modal.py
│   └── pages/
│       └── base_page.py     # Page object model
├── tests/
│   ├── conftest.py          # Pytest fixtures
│   ├── sign-up-TC.py        # Sign up test
│   ├── Sign-In-Invalid-Credentials-TC3.py  # Login test
│   └── reset-password-TC2.py # Reset password test
├── test-cases/              # Test case documentation
├── allure-results/          # Test execution results
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Key Technologies

- **Selenium** - Web browser automation
- **Pytest** - Test framework
- **Allure** - Test reporting and analytics
- **Python-dotenv** - Environment variable management

## Page Object Model (POM)

The project uses the Page Object Model pattern:

- **BasePage** - Represents the main page with common actions (Sign In, Sign Up, Reset Password buttons)
- **Components** - Reusable modal components with specific interactions
- **Tests** - Test cases that use pages and components

### Example Usage

```python
from src.pages.base_page import BasePage

# In test
page = BasePage(driver)
signin_modal = page.click_sign_in()
signin_modal.enter_email("test@example.com")
signin_modal.enter_password("password123")
signin_modal.click_sign_in()
```

## Test Cases

### 1. Sign Up Test (`sign-up-TC.py`)
- Opens Sign Up modal
- Enters valid email, username, and password
- Verifies modal closes after successful registration

### 2. Sign In with Invalid Credentials (`Sign-In-Invalid-Credentials-TC3.py`)
- Opens Sign In modal
- Enters invalid email and password
- Verifies error messages are displayed

### 3. Reset Password Test (`reset-password-TC2.py`)
- Opens Sign In modal
- Clicks Forgot Password link
- Enters email for password reset
- Verifies modal closes after submission

## Configuration Details

### Timeouts

- **IMPLICIT_WAIT_TIMEOUT**: Default wait time for elements (2 seconds)
- **EXPLICIT_WAIT_TIMEOUT**: Explicit wait for specific conditions (2 seconds)

Increase these values if you experience timeout errors on slower connections.

### Headless Mode

- **HEADLESS_MODE=False**: Browser window is visible during test execution
- **HEADLESS_MODE=True**: Browser runs in headless mode (no visible window)

## Troubleshooting

### ChromeDriver Version Mismatch

Ensure your ChromeDriver version matches your Google Chrome version. Download from: https://chromedriver.chromium.org/

### Import Errors

Make sure the virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Timeout Errors

- Increase timeout values in `.env` file
- Check your internet connection
- Verify the BASE_URL is accessible

### Test Failures in Headless Mode

Set `HEADLESS_MODE=False` to run tests with visible browser for debugging.

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure everything passes
4. Commit and push your changes
5. Create a Pull Request

## Author

Ihor Strakhov
