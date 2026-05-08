import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_comments_for_post():
    response = requests.get(f"{BASE_URL}/posts/1/comments")
    assert response.status_code == 200
    comments = response.json()
    assert isinstance(comments, list)
    assert comments[0]["postId"] == 1


def test_update_post():
    response = requests.put(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
