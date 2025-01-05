from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', views.ProductCreateView.as_view(), name='add_product'),
    path('edit_product/<int:pk>/', views.ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('add_category/', views.CategoryCreateView.as_view(), name='add_category'),
    path('edit_category/<int:pk>/', views.CategoryUpdateView.as_view(), name='edit_category'),
    path('delete_category/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),
]
