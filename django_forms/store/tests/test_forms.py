import pytest
from store.forms import ProductForm, CategoryForm


@pytest.mark.django_db
def test_product_form(category, form_data_product_form):
    form = ProductForm(data=form_data_product_form)
    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['name'] == form_data_product_form['name']
    assert cleaned_data['description'] == form_data_product_form['description']
    assert cleaned_data['price'] == form_data_product_form['price']
    assert cleaned_data['category'] == form_data_product_form['category']


@pytest.mark.django_db
def test_category_form(form_data_category_form):
    form = CategoryForm(data=form_data_category_form)
    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['name'] == form_data_category_form['name']
    assert cleaned_data['description'] == form_data_category_form['description']



@pytest.mark.parametrize("name, description, res",
    [
        ('Test cat', 'Test description', True),
        ('Te', 'Test description', False),
        ('Test cat', 'Test de', False),
    ]
)
@pytest.mark.django_db
def test_category_form_params(name, description, res):
    form_data = {'name': name, 'description': description}
    form = CategoryForm(data=form_data)
    assert form.is_valid() == res
