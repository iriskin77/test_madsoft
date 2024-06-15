from file_service.app.repository.minio.minio_storage import FileRepository, client
from file_service.app.repository.postgres.sql import SqlRepository
from file_service.app.config.config import FILE_PATH_UPLOAD_TMP, FILE_PATH_DOWNLOAD_TMP


class InitPostgresSQL:

    def __init__(self, session):
        self.session = session

    def get_postgres_sql(self) -> SqlRepository:
        return SqlRepository(session=self.session)


class InitMinioStorage:

    def __init__(self, client, file_path_upload: str, file_path_download: str):
        self._client = client
        self._file_path_upload = file_path_upload
        self.file_path_download = file_path_download

    def get_minio_storage(self) -> FileRepository:
        return FileRepository(client_minio=self._client,
                              file_path_upload=self._file_path_upload,
                              file_path_download=self.file_path_download,
                              )
    

minio_storage = InitMinioStorage(client=client,
                                 file_path_upload=FILE_PATH_UPLOAD_TMP,
                                 file_path_download=FILE_PATH_DOWNLOAD_TMP,)


class Container:

    def __init__(self, postgres: InitPostgresSQL, minio_storage: InitMinioStorage):
        self.postgres = postgres
        self.minio = minio_storage
