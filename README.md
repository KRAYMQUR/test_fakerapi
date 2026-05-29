# REST API Test Automation

![CI](https://github.com/KRAYMQUR/test_fakerapi/actions/workflows/ci_cd.yml/badge.svg)

Automated API tests for [FakeRestAPI](https://fakerestapi.azurewebsites.net) built with Python, pytest, and Allure reporting.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Language |
| pytest | Test framework |
| requests | HTTP client |
| pydantic | Response validation |
| allure-pytest | Test reporting |

---

## Project Structure

```
test_restapi/
├── api/
│   ├── base_api.py          # Base HTTP class
│   ├── books_api.py         # Books endpoints
│   └── authors_api.py       # Authors endpoints
├── models/
│   ├── book.py              # Pydantic model for Book
│   └── authors.py           # Pydantic model for Author
├── tests/
│   ├── test_books.py        # Positive tests for Books
│   ├── test_books_negative.py
│   ├── test_authors.py      # Positive tests for Authors
│   └── test_authors_negative.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running Tests

```bash
pytest
```

## Allure Report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## Test Coverage

| Resource | Methods | Positive | Negative |
|----------|---------|----------|----------|
| Books | GET, POST, PUT, DELETE | 5 | 4 |
| Authors | GET, POST, PUT, DELETE | 5 | 4 |

---

## CI/CD

Tests run automatically on every push to `main` via GitHub Actions.  
Allure report is published to [GitHub Pages](https://kraymqur.github.io/test_fakerapi).
