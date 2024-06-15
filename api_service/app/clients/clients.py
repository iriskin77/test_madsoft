import aiohttp
import aiofiles
from api_service.app.config.config import FILE_PATH_DOWNLOAD_TMP


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

    async def send_file(self, filepath: str, chunk_size: int):

        hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        "CONTENT-DISPOSITION": f"attachment;filename={filepath}"}

        print(filepath)

        with open(filepath, 'rb') as f:
            async with aiohttp.ClientSession() as session:
                async with session.post(url=self._url_post, headers=hdr, data={"file": f}) as resp:
                    return await resp.json()

    async def get_file(self, filename: str):

        hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',}
        #"CONTENT-DISPOSITION": f"attachment;filename={filepath}"}

        params = {"filename": filename}

        async with aiohttp.ClientSession() as session:
            async with session.get(url=self._url_get, params=params) as resp:

                if resp.status == 200:
                    f = await aiofiles.open(FILE_PATH_DOWNLOAD_TMP + filename, mode='wb')
                    await f.write(await resp.read())
                    await f.close()
                    return resp

                return resp.status

