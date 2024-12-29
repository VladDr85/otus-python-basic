import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_templates_product_list(client, product):
    url = reverse('product_list')
    response = client.get(url)
    assert response.status_code == 200
    assert "Список товаров" in response.content.decode()
    assert "Test Product" in response.content.decode()


@pytest.mark.django_db
def test_templates_category_list(client, category):
    url = reverse('category_list')
    response = client.get(url)
    assert response.status_code == 200
    assert "Список категорий" in response.content.decode()
    assert "Test Category" in response.content.decode()


