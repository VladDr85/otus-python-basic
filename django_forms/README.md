## Описание настройки и запуска приложения
- Каталог приложения: [`django_formsp`](https://github.com/VladDr85/otus-python-basic/tree/django_forms/django_forms)
- Применить миграции для создания БД и структуры: ``` python manage.py migrate ```
- Заполнить тестовыми данными: ``` python manage.py loaddata store/fixtures/store_fixture.json ```
- Запуск приложения: ``` python manage.py runserver ```
- Запуск всех тестов: ``` pytest -v store/tests ```
- SuperUser: `admin/admin`
- Установка Redis через Docker: 
  - docker run --name redis -d -p 6379:6379 redis
  - docker exec -it redis redis-cli ping


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
celery -A config worker --loglevel=info --pool=solo #запустить worker celery
celery -A config beat --loglevel=debug #запуск периодических задач
```
- Работа с проектом
```
python manage.py loaddata store/fixtures/store_fixture.json #заполнение данных из фикстур
python manage.py dumpdata store > store/fixtures/store_fixture_dump.json
python manage.py del_category_products #кастомная команда удаления Категорий и товаров
python manage.py generate_test_data #кастомная команда добавления товаров по существующим категориям 
```

## Домашнее задание: Задачи с Celery и Redis
### Цель
- Освоить использование Celery для выполнения фоновых задач и настройку Redis как брокера задач

### Результат:
- Приложение интернет-магазина с фоновыми задачами (например, отправка уведомлений при добавлении новых товаров).

### Описание/Пошаговая инструкция выполнения домашнего задания:
- **Настроить Celery и Redis**:
  - Установить Celery и Redis.
  - Подключить Redis как брокер задач для Celery.
- **Реализовать фоновую задачу**:
  - Создать задачу для логирования информации о добавлении нового товара.
  - Задача должна выводить сообщение на консоль (например, название нового товара).
- **Протестировать Celery**:
  - Убедиться, что задачи корректно ставятся в очередь и выполняются.

### Критерии оценки:
- Настроен Celery с Redis.
- Реализована и протестирована фоновая задача.

