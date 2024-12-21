### Описание приложения
- Каталог приложения: [`django_formsp`](https://github.com/VladDr85/otus-python-basic/tree/django_hw_1/django_1)
- Запуск приложения: ``` python manage.py runserver ```


### Цель
- Закрепить навыки работы с HTML-шаблонами, передачи данных из контроллеров в шаблоны и реализации форм для пользовательского ввода.

### Результат:
- Динамическое веб-приложение для интернет-магазина с отображением данных через шаблоны и возможностью добавления и редактирования товаров через формы.

### Описание/Пошаговая инструкция выполнения домашнего задания:
- **Создать шаблоны**:
  - Настроить базовый шаблон с использованием block и extends.
  - Создать страницу списка товаров (Product), где отображаются название, описание и цена.
  - Настроить страницу деталей товара с выводом всех данных.
- **Создать формы**:
  - Настроить форму для добавления нового товара.
  - Настроить форму для редактирования товара.
- **Связь с шаблонами**:
  - Настроить отображение ошибок валидации в шаблонах.
  - Реализовать обработку пользовательского ввода через контроллеры.
- **Настроить админку**:
  - Добавить кастомизацию: list_display, list_filter, search_fields.
  - Создать кастомные действия через `@admin.action`. Например, поменять цену или опубликовать товар.

### Критерии оценки:
- Реализованы шаблоны для списка и деталей товаров.
- Формы работают корректно, включая валидацию.
- Настройка админки с кастомизацией.

## Набор команд для выполнения ДЗ
- Создание и настройка проекта
```
pip install django
django-admin startproject config .	#создание проекта Django в текущем каталоге
python manage.py runserver
python manage.py startapp store		#создание приложения Django в текущем проекте
python manage.py makemigrations		#создать миграцию
python manage.py migrate		#применить все не примененные миграции
python manage.py createsuperuser
python manage.py shell
```
- Работа с проектом
```
from store.models import Product, Category
category = Category.objects.create(name='Телефон', description='Сотовые телефоны и смартфоны')
product = Product.objects.create(name='Samsung S24 DUO 254Gb', description = 'Samsung S24 DUO 254Gb Gray Exenus 2400', price=69999.99, category=category) 
Product.objects.all()
Category.objects.all()
category.products.all()
product.category.name
```