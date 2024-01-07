import os

import decouple


FILE_STORAGE_DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    decouple.config("FILE_STORAGE_DATA", default="data"),
)
FILE_STORAGE_TEMPLATES = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    decouple.config("FILE_STORAGE_TEMPLATES", default="TEMPLATES"),
)
FILE_NAME_PAGES = decouple.config("FILE_NAME_PAGES", default="pages")
ACCESS_TOKEN_BOT = decouple.config("ACCESS_TOKEN_BOT", default="SECRET_TOKEN")
ACCESS_TOKEN_USER = decouple.config("ACCESS_TOKEN_USER", default="SECRET_TOKEN")
ADMIN_ID = decouple.config("ADMIN_ID", cast=int, default=1)
GROUP_ID = decouple.config("GROUP_ID", cast=int, default=1)
TIMEZONE = decouple.config("TIMEZONE", default="Europe/Moscow")
DAY_POST = decouple.config("DAY_POST", default="12:00")
NIGHT_POST = decouple.config("NIGHT_POST", default="22:00")
