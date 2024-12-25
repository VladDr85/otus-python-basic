from django.shortcuts import render, get_object_or_404, redirect
from store.forms import ProductForm, CategoryForm
from store.models import Product, Category


def index(request):
    return render(request, 'store/home.html')

def product_list(request):
    products = Product.objects.all()
    context = {
        'title': 'Список товаров',
        'products': products,
    }
    return render(request, 'store/product_list.html', context=context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'title': product.name,
        'product': product
    }
    return render(request, 'store/product_detail.html', context=context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    context = {
        'title': 'Добавление товара',
        'form': form
    }
    return render(request, 'store/add_product.html', context=context)

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    context = {
        'title': 'Редактирование товара',
        'form': form
    }
    return render(request, 'store/edit_product.html', context=context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product.delete()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    context = {
        'title': 'Удаление товара',
        'form': form
    }
    return render(request, 'store/delete_product.html', context=context)

def category_list(request):
    categories = Category.objects.all()
    context = {
        'title': 'Список категорий',
        'categories': categories
    }
    return render(request, 'store/category_list.html', context=context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'title': category.name,
        'category': category
    }
    return render(request, 'store/category_detail.html', context=context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    context = {
        'title': 'Добавление категории',
        'form': form
    }
    return render(request, 'store/add_category.html', context=context)

def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    context = {
        'title': 'Редактирование категории',
        'form': form
    }
    return render(request, 'store/edit_category.html', context=context)

def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category.delete()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    context = {
        'title': 'Удаление категории',
        'form': form
    }
    return render(request, 'store/delete_category.html', context=context)
