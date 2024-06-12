import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

FILE_PATH_UPLOAD_TMP = os.path.join(BASE_DIR, "tmp", "upload/")
FILE_PATH_DOWNLOAD_TMP = os.path.join(BASE_DIR, "tmp", "download/")
