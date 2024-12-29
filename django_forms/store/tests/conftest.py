import pytest
from store.models import Product, Category


@pytest.fixture
def category():
    return Category.objects.create(
        name='Test Category',
        description='Test description',
    )


@pytest.fixture
def product(category):
    return Product.objects.create(
        name='Test Product',
        description='Test description',
        price=10,
        category=category,
    )


@pytest.fixture
def form_data_product_form(category):
    return {
        'name': 'Test ProductForm',
        'description': 'Test description ProductForm',
        'price': 10,
        'category': category,
    }


@pytest.fixture
def form_data_category_form():
    return {
        'name': 'Test CategoryForm',
        'description': 'Test description CategoryForm',
    }