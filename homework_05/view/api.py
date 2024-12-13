from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Form
from fastapi.requests import Request

from models.contact import Contact

api_router = APIRouter(prefix="/api", tags=["API"])
templates = Jinja2Templates(directory='templates')


@api_router.get(
    "/contacts",
    response_class=HTMLResponse,
    summary='Получение всех контактов',
    description='Возвращаем все записи из файла с контактами'
)
def get_contacts(request: Request):
    contacts = Contact.get_all_contacts()
    context = {
        'request': request,
        'title': 'Contact List',
        'contacts': contacts}
    return templates.TemplateResponse('contacts.html', context=context)


@api_router.get(
    "/contact/{contact_id}",
    response_class=HTMLResponse,
    summary='Получение одного контакта',
    description='Возвращаем информацию по одному контакту, через ID'
)
def get_contact(request: Request, contact_id: int):
    contact = Contact.get_contacts_by_id(contact_id)
    print(f'Контакт {contact}')
    context = {
        'request': request,
        'title': 'Contact info',
        'contact': contact}
    return templates.TemplateResponse('contacts.html', context=context)

@api_router.post(
    "/add-contact-query",
    summary='Добавление нового контакта',
    description='Добавление нового контакта и запись в файл'
)
def add_contact_query(name: str, phone: str, email: str, status: str, city: str):
    new_contact = Contact.add_contact(name, phone, email, status, city)
    if "error" in new_contact:
        return {"message": "Данные не прошли валидацию!", "record": new_contact}
    return {"message": "Запись успешно добавлена!", "record": new_contact}

@api_router.post(
    "/add-contact",
    response_class=HTMLResponse,
    summary="Добавление нового контакта через Web",
    description='Добавление нового контакта и запись в файл. Возвращает обновленный список записей в формате HTML',
)
def add_contact(request: Request, name: str = Form(...), phone: str = Form(...), email: str = Form(...), status: str = Form(...), city: str = Form(...)):
    new_contact = Contact.add_contact(name, phone, email, status, city)
    contacts = Contact.get_all_contacts()
    if "error" in new_contact:
        target = new_contact["error"][0]["input"]
        error = new_contact["error"][0]["msg"]
        message = f"Error! Validation error, {target} - {error}"
    else:
        message = "Запись успешно добавлена!"
    context = {
        "request": request,
        "contacts": contacts,
        "message": message,
    }
    return templates.TemplateResponse('contacts.html', context=context)

@api_router.delete(
    "/delete-contact",
    summary="Удаление записи через Query String",
    description="Удаляет запись из файла через Query String.",
)
def delete_contact(contact_id: int):
    message = Contact.delete_contact(contact_id_del=contact_id)
    return message
