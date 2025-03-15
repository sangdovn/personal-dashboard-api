from tests.utils import client
from fastapi import status

def test_youtube():
    response = client.get("/youtube")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == { "message": "Hello YouTube" }