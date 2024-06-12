import os
from pathlib import Path


FILE_SERVICE_URL_GET: str = "http://localhost:10001/get_file"
FILE_SERVICE_URL_POST: str = "http://localhost:10001/save_file"
FILE_SERVICE_URL_PUT: str = "http://localhost:10001/update_file"
FILE_SERVICE_URL_DELETE: str = "http://localhost:10001/delete_file"


BASE_DIR = Path(__file__).resolve().parent.parent

FILE_PATH_UPLOAD_TMP = os.path.join(BASE_DIR, "tmp", "upload/")
FILE_PATH_DOWNLOAD_TMP = os.path.join(BASE_DIR, "tmp", "download/")
