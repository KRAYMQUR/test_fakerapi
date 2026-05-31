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
| faker | Dynamic test data generation |
| allure-pytest | Test reporting |
| python-dotenv | Environment configuration |

---

## Project Structure

```
test_restapi/
├── api/
│   ├── base_api.py              # Base HTTP class with session and type hints
│   ├── books_api.py             # Books endpoints
│   └── authors_api.py           # Authors endpoints
├── models/
│   ├── book.py                  # Pydantic model for Book
│   └── authors.py               # Pydantic model for Author
├── tests/
│   ├── constants.py             # Shared test IDs
│   ├── test_books.py            # Positive tests for Books
│   ├── test_books_negative.py   # Negative tests for Books
│   ├── test_authors.py          # Positive tests for Authors
│   └── test_authors_negative.py # Negative tests for Authors
├── conftest.py                  # Fixtures (session-scoped API clients, yield fixtures)
├── pytest.ini                   # Markers and default options
├── .env.example                 # Environment variable template
└── requirements.txt
```

---

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

```bash
cp .env.example .env
```

`.env`:
```
BASE_URL=https://fakerestapi.azurewebsites.net/api/v1
```

---

## Running Tests

```bash
# All tests
pytest

# Smoke only
pytest -m smoke

# Regression only
pytest -m regression
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
| Books | GET, POST, PUT, DELETE | 5 | 3 |
| Authors | GET, POST, PUT, DELETE | 5 | 3 |

**Patterns used:**
- Faker for dynamic test data
- Pydantic for response contract validation
- `yield` fixtures for test data creation (test itself is the teardown)
- `xfail` for known API bugs
- Response time assertions on smoke tests
- `logging` for request/response visibility
- Parametrize for boundary coverage

---

## CI/CD

Tests run automatically on every push to `main` via GitHub Actions.  
Allure report is published to [GitHub Pages](https://kraymqur.github.io/test_fakerapi).
