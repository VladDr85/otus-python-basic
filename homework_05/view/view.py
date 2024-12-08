from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from fastapi.requests import Request


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get('/')
def get_home(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request, 'title': 'Home'})

@router.get("/about")
def get_about(request: Request):
    return templates.TemplateResponse('about.html',
                                      {'request': request, 'title': 'Home'})
