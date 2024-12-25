from fastapi import APIRouter

view_router = APIRouter(tags=["views"])


@view_router.get("/")
async def ping():
    return {"message": "Hello"}


@view_router.get("/ping")
async def ping():
    return {"message": "pong"}
