# Домашнее задание

Создание проекта, работа с моделями и продвинутая настройка админки

## Цель:
Закрепить навыки создания проекта и приложения в Django, работы с моделями через ORM, а также настройки админки для удобной работы с данными.

## Результат:
Рабочий проект Django с подключённой базой данных, продвинутой настройкой админки, кастомными командами и генерацией данных через фабрики.

## Описание/Пошаговая инструкция выполнения домашнего задания:
### Создать Django проект и приложение:
Настроить новый проект Django.
Добавить приложение (например, store).
### Создать модели:
Модель Product с полями: name, description, price, created_at.
Модель Category с полями: name, description.
Связать Product с Category через ForeignKey.
### Выполнить миграции:
Создать и применить миграции.
### Работа с ORM:
Создать записи для моделей, используя кастомную команду.

## Описание
Django==5.1.4
Каталог приложения home_w\django_1

Запуск приложения по команде: python manage.py runserver

Кастомные команды еще не пройдены поэтому был использован shell

## Набор команд для выполнения ДЗ
pip install django

django-admin startproject config .	#создание проекта Django в текущем каталоге

python manage.py runserver

python manage.py startapp store		#создание приложения Django в текущем проекте

python manage.py makemigrations		#создать миграцию

python manage.py migrate			#применить все не примененные миграции

python manage.py createsuperuser

python manage.py shell

from store.models import Product, Category

category = Category.objects.create(name='Телефон', description='Сотовые телефоны и смартфоны')

product = Product.objects.create(name='Samsung S24 DUO 254Gb', description = 'Samsung S24 DUO 254Gb Gray Exenus 2400', price=69999.99, category=category) 

Product.objects.all()

Category.objects.all()

category.products.all()

product.category.name