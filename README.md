# API Testing Project

This project demonstrates API testing using two popular frameworks: pytest (Python) and Robot Framework.

## Overview

The project tests the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API, a free fake API for testing and prototyping.

## Project Structure

- `pytest_tests/`: Contains pytest-based API tests.
  - `conftest.py`: Pytest configuration and fixtures.
  - `test_auth.py`: Authentication-related tests (placeholder).
  - `test_tasks.py`: Tests for posts, comments, etc.
- `robot_tests/`: Contains Robot Framework tests.
  - `task_api.robot`: Robot test cases for the API.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/TintuJ/API_Testing.git
   cd API_Testing
   ```

2. Set up a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install requests pytest robotframework-requests
   ```

## Running Tests

### Pytest Tests

Run all pytest tests:
```
pytest pytest_tests/
```

### Robot Framework Tests

Run Robot tests:
```
robot robot_tests/task_api.robot
```

Reports will be generated in the respective directories.

## Contributing

Feel free to add more test cases or improve the existing ones.