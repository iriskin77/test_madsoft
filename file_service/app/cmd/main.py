from fastapi import FastAPI
from file_service.app.handlers.handlers import router_file

app = FastAPI()

app.include_router(router_file)
