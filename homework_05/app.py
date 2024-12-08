from fastapi import FastAPI
from pydantic import BaseModel
from view.view import router

app = FastAPI()
app.include_router(router)


class Contact(BaseModel):
    name: str
    phone: str
    email: str | None
    status: str | None
    city: str | None


class Task(BaseModel):
    name: str
    description: str | None


@app.get("/")
def get_root():
    return {"data": "Hello World !"}





@app.get("/contacts")
def get_contacts():
    contact = Contact(name='Имя',
                      phone='+79187887999',
                      email='mymail@mail.com',
                      status='friend',
                      city='New York')
    return {"data": contact}


@app.get("/tasks")
def get_tasks():
    tasks = Task(name='Example',
                 description='c')
    return {"data": tasks}


"""
Домашнее задание №5
Первое веб-приложение

- в модуле `app` создайте базовое FastAPI приложение
- создайте обычные представления
  - создайте index view `/`
  - добавьте страницу `/about/`, добавьте туда текст, информацию о сайте и разработчике
  - создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
  - в базовый шаблон подключите статику Bootstrap 5 (подключите стили), примените стили Bootstrap
  - в базовый шаблон добавьте навигационную панель `nav` (https://getbootstrap.com/docs/5.0/components/navbar/)
  - в навигационную панель добавьте ссылки на главную страницу `/` и на страницу `/about/` при помощи `url_for`
  - добавьте новые зависимости в файл `requirements.txt` в корне проекта
    (лучше вручную, но можно командой `pip freeze > requirements.txt`, тогда обязательно проверьте, что туда попало, и удалите лишнее)
- создайте api представления:
  - создайте api router, укажите префикс `/api`
  - добавьте вложенный роутер для вашей сущности (если не можете придумать тип сущности, рассмотрите варианты: товар, книга, автомобиль)
  - добавьте представление для чтения списка сущностей
  - добавьте представление для чтения сущности
  - добавьте представление для создания сущности
"""
