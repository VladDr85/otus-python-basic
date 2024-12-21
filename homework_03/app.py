from fastapi import FastAPI

from view.views import view_router

app = FastAPI(
    title='Домашнее задание №5',
    description='Домашнее задание "Docker контейнер c веб-приложением"',
    version='1.0.0',
)

app.include_router(view_router)
