import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["id"] == 1


def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "username" in data


def test_create_post():
    response = requests.post(f"{BASE_URL}/posts", json={
        "userId": 1,
        "title": "Test Post",
        "body": "This is a test post."
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Post"
