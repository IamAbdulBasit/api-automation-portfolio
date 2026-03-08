# API Automation Portfolio

## Overview

This project demonstrates **API automation testing using Postman and Python**.
It shows two approaches to testing APIs:

1. **Postman Collection + Newman** for API test execution and reporting.
2. **Python + Pytest + Requests** for building a lightweight API automation framework.

The goal of this repository is to showcase practical API testing skills used by QA engineers in real-world projects.

---

# Project Structure

```
api-automation-portfolio
│
├── api-automation-postman
│   ├── collections
│   ├── environments
│
├── api-automation-python
│   ├── tests
│   ├── utils
│   └── requirements.txt
│
└── README.md
```

### Folder Details

**api-automation-postman**

Contains Postman API test collections and environment files.

Tests include:

* API request validation
* Response status verification
* Response body validation
* Authentication testing

These tests are executed using **Newman CLI**.

---

**api-automation-python**

Python-based API test framework using:

* `pytest`
* `requests`

Tests include:

* API endpoint validation
* Response status checks
* Response data validation
* JSON schema validation

---

# Prerequisites

Install the following tools:

* Python 3.x
* Node.js
* npm
* Postman (optional for editing collections)

---

# Setup

Clone the repository:

```
git clone https://github.com/IamAbdulBasit/api-automation-portfolio.git
```

Navigate into the project:

```
cd api-automation-portfolio
```

---

# Running Python API Tests

Navigate to the Python project:

```
cd api-automation-python
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the tests:

```
pytest
```

Example output:

```
================== test session starts ==================
collected 3 items

tests/test_users.py .... PASSED
tests/test_login.py .... PASSED

================== 3 passed in 1.25s ==================
```

---

# Screenshot: Pytest Passing Tests

Add a screenshot of your successful pytest run.

Example:

```
docs/pytest-success.png
```

![Pytest Passing Tests](docs/pytest-success.png)

---

# Running Postman Tests with Newman

Install Newman globally:

```
npm install -g newman
```

Run the Postman collection:

```
newman run api-automation-postman/collections/api_tests_collection.json
```

To generate an HTML report:

```
newman run api-automation-postman/collections/api_tests_collection.json \
-r html \
--reporter-html-export reports/newman-report.html
```

---

# Newman HTML Report

After execution, the report will be generated at:

```
reports/newman-report.html
```

Open the file in a browser to view the detailed results.

---

# Screenshot: Newman HTML Report

Add a screenshot of the generated report.

Example:

```
docs/newman-report.png
```

![Newman Report](docs/newman-report.png)

---

# Key Skills Demonstrated

This project demonstrates the following QA automation skills:

* API test design
* Postman collection development
* Automated API validation
* Python API testing using pytest
* CLI test execution using Newman
* Automated report generation

---

# Future Improvements

Planned enhancements:

* CI/CD integration
* Data-driven API tests
* Environment configuration
* Performance testing integration
* Docker test execution

---

# Author

Abdul Basit
QA Engineer
API Testing | Automation | Python
