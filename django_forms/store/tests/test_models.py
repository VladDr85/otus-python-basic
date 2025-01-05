import pytest
from store.models import Category, Product


@pytest.mark.django_db
def test_category_creation(category):
    assert Category.objects.count() == 1
    assert category.name == 'Test Category'
    assert category.description == 'Test description'
    assert str(category) == 'Test Category'


@pytest.mark.django_db
def test_product_creation(product, category):
    assert Product.objects.count() == 1
    assert product.name == 'Test Product'
    assert product.description == 'Test description'
    assert product.price == 10
    assert product.category.name == 'Test Category'
    assert str(product) == 'Test Product, цена: 10 p.'
