from api_service.app.config.config import (
    FILE_SERVICE_URL_GET,
    FILE_SERVICE_URL_POST,
    FILE_SERVICE_URL_PUT,
    FILE_SERVICE_URL_DELETE,
)
from api_service.app.clients.clients import FileServiceClient
from api_service.app.services.services import FileService


class Container:

    def __init__(self, client: FileServiceClient):
        self._client = client

    def get_service(self) -> FileService:
        return FileService(self._client)


client = FileServiceClient(
    url_fileservice_get=FILE_SERVICE_URL_GET,
    url_fileservice_post=FILE_SERVICE_URL_POST,
    url_fileservice_put=FILE_SERVICE_URL_PUT,
    url_fileservice_delete=FILE_SERVICE_URL_DELETE,
)

container = Container(client=client)
