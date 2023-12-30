import os
import decouple

FILE_STORAGE_DATA = os.path.join(
    os.getcwd(),
    decouple.config("FILE_STORAGE_DATA"),
)
FILE_NAME_PAGES = decouple.config("FILE_NAME_PAGES")
