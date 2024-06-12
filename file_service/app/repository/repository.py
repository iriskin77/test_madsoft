from abc import abstractmethod, ABC
from typing import Generic, Type, TypeVar, Union, Sequence
from pydantic import BaseModel
from minio import Minio


client = Minio("localhost:9000", access_key="minio_user", secret_key="minio_password", secure=False)


class Repository(ABC):

    @abstractmethod
    def get(self, object_name: str, file_path: str):
        raise NotImplementedError

    @abstractmethod
    def get_list_files(self):
        raise NotImplementedError

    @abstractmethod
    def create(self, file_name: str, file_path: str):
        raise NotImplementedError

    @abstractmethod
    def put(self):
        raise NotImplementedError

    @abstractmethod
    def patch(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self, object_name: str):
        raise NotImplementedError


ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class FileRepository(Repository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, client_minio: Minio, bucket_name: str):
        self._client = client_minio
        self._bucket_name = bucket_name

    async def get(self,  object_name: str, file_path: str):
        path_download_tmp_dir = file_path + object_name
        file = self._client.fget_object(bucket_name=self._bucket_name,
                                        object_name=object_name,
                                        file_path=path_download_tmp_dir)

        return file

    async def get_list_files(self):
        files = self._client.list_objects(bucket_name=self._bucket_name, recursive=True)
        print(files)
        return files

    async def create(self, file_name: str, file_path: str):

        found = client.bucket_exists(self._bucket_name)
        if not found:
            client.make_bucket(self._bucket_name)

        self._client.fput_object(bucket_name=self._bucket_name,
                                 object_name=file_name,
                                 file_path=file_path)
        return True

    async def put(self):
        pass

    async def patch(self):
        pass

    async def delete(self, object_name: str):
        self._client.remove_object(bucket_name=self._bucket_name,
                                   object_name=object_name)
        return True