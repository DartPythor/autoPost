import os
import pickle

import config


class FileManager:
    def __init__(self, pathfile=None):
        self.pathfile = pathfile
        self.filetype = ".pickle"

        if self.pathfile is None:
            self.pathfile = config.FILE_STORAGE_DATA

    def get_path(self):
        return (
            os.path.join(
                self.pathfile,
                config.FILE_NAME_PAGES,
            )
            + self.filetype
        )

    def _save(self, data):
        with open(self.get_path(), mode="wb") as file:
            pickle.dump(data, file)

    def _load(self) -> any:
        with open(self.get_path(), mode="rb") as file:
            return pickle.load(file)

    def _create_file(self):
        data = {
            "index_page": 0,
            "apcontinue": "",
            "pages": [],
        }
        self._save(data)

    def load(self):
        if not os.path.isfile(self.get_path()):
            self._create_file()
        return self._load()

    def save(self, data):
        self._save(data)
