from fastapi import FastAPI
from app.routers.routes import router

app = FastAPI()

app.include_router(router=router)