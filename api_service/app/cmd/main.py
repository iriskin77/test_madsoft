from fastapi import FastAPI
from app.handlers.handlers import router_file



app = FastAPI()

app.include_router(router_file)


