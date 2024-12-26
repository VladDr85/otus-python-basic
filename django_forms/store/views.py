from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from store.forms import ProductForm, CategoryForm
from store.models import Product, Category


def index(request):
    return render(request, 'store/home.html')


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    extra_context = {
        'title': 'Список товаров',
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        max_price = self.request.GET.get('price')

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'
    extra_context = {
        'title': 'Описание товара',
    }


class ProductCreateView(CreateView):
    model = Product
    template_name = 'store/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    extra_context = {
        'title': 'Создание товара',
    }

    def form_valid(self, form):
        messages.success(self.request, 'Товар успешно создан')
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'store/edit_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    extra_context = {
        'title': 'Редактирование товара',
    }


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/delete_product.html'
    success_url = reverse_lazy('product_list')
    extra_context = {
        'title': 'Удаление товара',
    }


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
