from http.client import responses

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from store.forms import ProductForm, CategoryForm
from store.models import Product, Category
from store.tasks import send_notification_email

def index(request):
    return render(request, 'store/home.html')


class ProductListView(ListView):
    """
    Класс для отображения списка товаров с включенной пагинацией.
    В get_queryset настроена фильтрация по Категории и Цене.
    В get_context_data дополняем контекст, чтобы вернуть список Категорий для фильтрации
    """
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    paginate_by = 4
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
    """
    Класс для детального отображения информации о конкретном продукте
    """
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'
    extra_context = {
        'title': 'Описание товара',
    }


class ProductCreateView(CreateView):
    """
    Класс для создания нового товара.
    После успешного создания товара, выводится сообщение на странице product_list
    Отправляется письмо на почту с информацией о новом товаре
    """
    model = Product
    template_name = 'store/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    extra_context = {
        'title': 'Создание товара',
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        send_notification_email.delay(
            subject = f'Создание товара: {form.instance.name}',
            message = f'Товар был создан с описанием: {form.instance.description}',
            recipient_list = 'skoch2000@yandex.ru',
        )

        product_name = form.cleaned_data['name']
        messages.success(self.request, f'Товар "{product_name}" успешно создан!')
        return response


class ProductUpdateView(UpdateView):
    """
    Класс для обновления товара.
    После успешного обновления, выводится сообщение на странице product_list
    """
    model = Product
    template_name = 'store/edit_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    extra_context = {
        'title': 'Редактирование товара',
    }

    def form_valid(self, form):
        product_name = form.cleaned_data['name']
        messages.success(self.request, f'Товар "{product_name}" успешно обновлен!')
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    """
    Класс для удаления товара.
    """
    model = Product
    template_name = 'store/delete_product.html'
    success_url = reverse_lazy('product_list')
    extra_context = {
        'title': 'Удаление товара',
    }


class CategoryListView(ListView):
    """
    Класс для отображения списка категорий товаров с включенной пагинацией.
    """
    model = Category
    template_name = 'store/category_list.html'
    context_object_name = 'categories'
    paginate_by = 3
    extra_context = {
        'title': 'Список категорий',
    }


class CategoryDetailView(DetailView):
    """
    Класс для детального отображения информации о конкретной категории товара
    """
    model = Category
    template_name = 'store/category_detail.html'
    context_object_name = 'category'
    extra_context = {
        'title': 'Описание категории',
    }


class CategoryCreateView(CreateView):
    """
    Класс для создания новой категории товара.
    После успешного создания категории, выводится сообщение на странице category_list
    """
    model = Category
    template_name = 'store/add_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')
    extra_context = {
        'title': 'Создание категории',
    }

    def form_valid(self, form):
        category_name = form.cleaned_data['name']
        messages.success(self.request, f'Категория "{category_name}" успешно создана!')
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    """
    Класс для обновления категорий.
    После успешного обновления, выводится сообщение на странице category_list
    """
    model = Category
    template_name = 'store/edit_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')
    extra_context = {
        'title': 'Редактирование категории',
    }

    def form_valid(self, form):
        category_name = form.cleaned_data['name']
        messages.success(self.request, f'Категория "{category_name}" успешно обновлена!')
        return super().form_valid(form)


class CategoryDeleteView(DeleteView):
    """
    Класс для удаления категории товара.
    """
    model = Category
    template_name = 'store/delete_category.html'
    success_url = reverse_lazy('category_list')
    extra_context = {
        'title': 'Удаление категории',
    }
