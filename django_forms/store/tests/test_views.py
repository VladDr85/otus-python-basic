import pytest
from django.urls import reverse

from store.models import Category, Product


@pytest.mark.django_db
def test_category_create_view(mocker, client):
    category = Category.objects.create(
        name='Test Category mocker',
        description='Test Category mocker',
    )
    mocker_create = mocker.patch('store.models.Product.save')

    url = reverse('add_product')
    data_product = {
        'name': 'Test Product mocker',
        'description': 'Test Product mocker',
        'price': 20,
        'category': category.id,
    }
    response = client.post(url, data_product)

    assert mocker_create.call_count == 1
    assert response.status_code == 302


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "Phone-tik" in response.content.decode()


@pytest.mark.django_db
def test_product_list(client):
    url = reverse('product_list')
    response = client.get(url)
    assert response.status_code == 200
    assert "Список товаров" in response.content.decode()


@pytest.mark.django_db
def test_product_detail(client, product):
    url = reverse('product_detail', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 200
    assert "Описание товара" in response.content.decode()


@pytest.mark.django_db
def test_add_product(client, product):
    url = reverse('add_product')
    response = client.get(url)
    assert response.status_code == 200
    assert "Создание товара" in response.content.decode()


@pytest.mark.django_db
def test_edit_product(client, product):
    url = reverse('edit_product', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 200
    assert "Редактирование товара" in response.content.decode()


@pytest.mark.django_db
def test_delete_product(client, product):
    url = reverse('delete_product', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 200
    assert "Удаление товара" in response.content.decode()


@pytest.mark.django_db
def test_category_list(client):
    url = reverse('category_list')
    response = client.get(url)
    assert response.status_code == 200
    assert "Список категорий" in response.content.decode()


@pytest.mark.django_db
def test_category_detail(client, product):
    url = reverse('category_detail', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 200
    assert "Описание категории" in response.content.decode()


@pytest.mark.django_db
def test_add_category(client, product):
    url = reverse('add_category')
    response = client.get(url)
    assert response.status_code == 200
    assert "Создание категории" in response.content.decode()


@pytest.mark.django_db
def test_edit_category(client, product):
    url = reverse('edit_category', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 200
    assert "Редактирование категории" in response.content.decode()


@pytest.mark.django_db
def test_delete_category(client, product):
    url = reverse('delete_category', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 200
    assert "Удаление категории" in response.content.decode()
