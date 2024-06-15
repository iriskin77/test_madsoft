from file_service.app.repository.repository import Repository, FileRepository, client
from file_service.app.config.config import FILE_PATH_UPLOAD_TMP, FILE_PATH_DOWNLOAD_TMP


class Container:

    def __init__(self, client, bucket_name: str, file_path_upload: str, file_path_download: str):
        self._client = client
        self._bucket_name = bucket_name
        self._file_path_upload = file_path_upload
        self.file_path_download = file_path_download

    def get_repository(self) -> FileRepository:
        return FileRepository(client_minio=self._client,
                              bucket_name=self._bucket_name,
                              file_path_upload=self._file_path_upload,
                              file_path_download=self.file_path_download,
                              )
    

container = Container(client=client,
                      bucket_name="filestorage",
                      file_path_upload=FILE_PATH_UPLOAD_TMP,
                      file_path_download=FILE_PATH_DOWNLOAD_TMP,)
