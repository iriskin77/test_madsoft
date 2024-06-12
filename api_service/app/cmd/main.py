from fastapi import FastAPI
from api_service.app.handlers.handlers import router_file

app = FastAPI()

app.include_router(router_file)
