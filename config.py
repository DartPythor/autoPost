import os

import decouple


FILE_STORAGE_DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    decouple.config("FILE_STORAGE_DATA", default="data"),
)
FILE_NAME_PAGES = decouple.config("FILE_NAME_PAGES", default="pages")
ACCESS_TOKEN_BOT = decouple.config("ACCESS_TOKEN_BOT")
ACCESS_TOKEN_USER = decouple.config("ACCESS_TOKEN_USER")
ADMIN_ID = decouple.config("ADMIN_ID", cast=int)
GROUP_ID = decouple.config("GROUP_ID", cast=int)
