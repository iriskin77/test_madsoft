from typing import Generator
import aiofiles
import aiohttp


class FileServiceClient:

    def __init__(self,
                 url_fileservice_get: str,
                 url_fileservice_post: str,
                 url_fileservice_put: str,
                 url_fileservice_delete: str) -> None:

        self._url_get = url_fileservice_get
        self._url_post = url_fileservice_post
        self._url_put = url_fileservice_put
        self._url_delete = url_fileservice_delete

    async def _file_sender(self, file_name: str, chunk_size: int) -> Generator[bytes, None, None]:

        async with aiofiles.open(file_name, 'rb') as f:
            chunk = await f.read(chunk_size)

            while chunk:
                yield chunk
                chunk = await f.read(chunk_size)

    async def send_file(self, filepath: str, chunk_size: int):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                self._url_post,
                data=self._file_sender(file_name=filepath, chunk_size=chunk_size)
            ) as resp:
                return resp.status

    async def get_file(self):
        pass
