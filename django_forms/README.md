## Описание настройки и запуска приложения
- Каталог приложения: [`django_formsp`](https://github.com/VladDr85/otus-python-basic/tree/django_forms/django_forms)
- Применить миграции для создания БД и структуры: ``` python manage.py migrate ```
- Заполнить тестовыми данными: ``` python manage.py loaddata store/fixtures/store_fixture.json ```
- Запуск приложения: ``` python manage.py runserver ```
- Запуск всех тестов: ``` pytest -v store/tests ```
- SuperUser: `admin/admin`

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
python manage.py loaddata store/fixtures/store_fixture.json #заполнение данных из фикстур
python manage.py dumpdata store > store/fixtures/store_fixture_dump.json
python manage.py del_category_products #кастомная команда удаления Категорий и товаров
python manage.py generate_test_data #кастомная команда добавления товаров по существующим категориям 
```

## Домашнее задание: Class-Based Views и тестирование
### Цель
- Закрепить навыки работы с CBV (Class-Based Views) и написания автотестов с использованием Pytest.

### Результат:
- Приложение интернет-магазина с функциональностью CRUD через CBV и тестами для ключевых функций.

### Описание/Пошаговая инструкция выполнения домашнего задания:
- **Реализовать CBV**:
  - Использовать ListView для отображения списка товаров.
  - Настроить DetailView для отображения деталей товара.
  - Реализовать CreateView и UpdateView для добавления и редактирования товаров.
  - Добавить DeleteView для удаления товара.
- **Написать тесты для приложения**:
  - Тесты для моделей: проверить операции создания, чтения, обновления и удаления записей.

### Критерии оценки:
- Реализованы CBV для CRUD-операций.
- Написаны тесты.

