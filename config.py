import decouple
import os

FILE_STORAGE_DATA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    decouple.config("FILE_STORAGE_DATA"),
)
FILE_NAME_PAGES = decouple.config("FILE_NAME_PAGES")
