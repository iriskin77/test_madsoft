import os
from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


BASE_DIR = Path(__file__).resolve().parent.parent

FILE_PATH_UPLOAD_TMP = os.path.join(BASE_DIR, "tmp", "upload/")
FILE_PATH_DOWNLOAD_TMP = os.path.join(BASE_DIR, "tmp", "download/")


POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

DATABASE_URL_POSTGRES = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}?async_fallback=True"

engine = create_async_engine(DATABASE_URL_POSTGRES, echo=False, future=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine, class_=AsyncSession)
