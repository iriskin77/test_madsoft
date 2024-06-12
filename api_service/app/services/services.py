import os
import random
import aiofiles
from fastapi import File
import string
from abc import abstractmethod, ABC
from api_service.app.clients.clients import FileServiceClient
from api_service.app.config.config import FILE_PATH_UPLOAD_TMP, FILE_PATH_DOWNLOAD_TMP


class Service(ABC):

    @abstractmethod
    def insert_file(self, file: File):
        raise NotImplementedError

    @abstractmethod
    def get_file_by_id(self, bucket_name: str, object_name: str):
        raise NotImplementedError

    def get_list_files(self, bucket_name: str):
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, bucket_name: str, object_name: str):
        raise NotImplementedError


class FileService(Service):

    def __init__(self, file_client: FileServiceClient):
        self._file_client = file_client

    async def insert_file(self, file: File):

        if not os.path.isdir(FILE_PATH_UPLOAD_TMP):
            os.mkdir(FILE_PATH_UPLOAD_TMP)

        filename_path = FILE_PATH_UPLOAD_TMP + file.filename

        async with aiofiles.open(filename_path, "wb") as buffer:
            data = await file.read()
            await buffer.write(data)

        res = await self._file_client.send_file(filepath=file.filename, chunk_size=file.size)
        return res

    async def get_file_by_id(self, bucket_name: str, object_name: str):
        raise NotImplementedError

    async def get_list_files(self, bucket_name: str):
        raise NotImplementedError

    async def delete_file(self, bucket_name: str, object_name: str):
        raise NotImplementedError
