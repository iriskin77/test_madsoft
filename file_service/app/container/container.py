from app.repository.repository import Repository, FileRepository, client 



class Container:

    def __init__(self, client, bucket_name: str):
        self._client = client
        self._bucket_name = bucket_name

    def get_repository(self) -> FileRepository:
        return FileRepository(client_minio=self._client,
                              bucket_name=self._bucket_name)
    

container = Container(client=client,
                      bucket_name="filestorage")