import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def auth_token():
    # register user
    requests.post(f"{BASE_URL}/auth/register", json={
        "username": "testuser",
        "password": "test123"
    })

    # login
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "username": "testuser",
        "password": "test123"
    })

    return response.json()["access_token"]


@pytest.fixture
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}