import pytest

from django.urls import reverse


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "Phone-tik" in response.content.decode()

