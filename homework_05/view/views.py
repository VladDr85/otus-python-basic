from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from fastapi.requests import Request


view_router = APIRouter(tags=["HTML"])
templates = Jinja2Templates(directory='templates')


@view_router.get(
    '/',
    summary='Маршрут для домашней страницы',
    description='Возвращает домашнюю страницу'
)
def get_home(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request, 'title': 'Home'})


@view_router.get(
    '/about',
    summary='Маршрут для about',
    description='Возвращает страницу "О сайте"'
)
def get_about(request: Request):
    return templates.TemplateResponse('about.html',
                                      {'request': request, 'title': 'About'})
