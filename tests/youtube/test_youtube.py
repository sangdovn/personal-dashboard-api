from fastapi import status

from tests.utils import client


def test_youtube():
    response = client.get("/youtube")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello YouTube"}
