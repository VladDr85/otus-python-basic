from django.contrib import admin
from store.models import Product, Category
from django_celery_results.models import TaskResult

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)
    search_help_text = 'Поиск по Имени и Описанию'
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'category',)
    search_fields = ('name', 'description', 'price',)
    search_help_text = 'Поиск по Имени, Описанию и Цене'
    ordering = ('category', 'price',)
    list_filter = ('category', )
    date_hierarchy = 'created_at'

    fields = ('name', 'description', 'price', 'category', 'created_at')
    readonly_fields = ('created_at',)

    @admin.action(description='Красивая цена')
    def get_beautiful_price(self, request, queryset):
        for product in queryset:
            product.price = round(product.price) - 0.01
            product.save()
        self.message_user(request, f'Обновили цену у {queryset.count()} продуктов')

    @admin.action(description='Скидка в 10%% и Красивая цена')
    def discount_ten_beautiful_price(self, request, queryset):
        for product in queryset:
            product.price = round(product.price * 0.9) - 0.01
            product.save()
        self.message_user(request, f'Сделали скидку на 10% и выставили красивую цену у {queryset.count()} продуктов')

    @admin.action(description='Наценка в 10%% и Красивая цена')
    def markup_ten_beautiful_price(self, request, queryset):
        for product in queryset:
            product.price = round(product.price * 1.1) - 0.01
            product.save()
        self.message_user(request, f'Наценка в 10% и красивая цена у {queryset.count()} продуктов')

    actions = [get_beautiful_price, discount_ten_beautiful_price, markup_ten_beautiful_price]
