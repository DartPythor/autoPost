import os
import pickle


class FileManager:
    def __init__(self, pathfile: str = os.getcwd()):
        self.pathfile = pathfile

    def save(self, data: any, filename: str) -> str:
        with open(os.path.join(self.pathfile, filename) + ".pickle", mode="wb") as file:
            pickle.dump(data, file)
        return os.path.join(self.pathfile, filename)

    def load(self, filename: str) -> any:
        with open(os.path.join(self.pathfile, filename) + ".pickle", mode="rb") as file:
            return pickle.load(file)


if __name__ == "__main__":
    filemanager = FileManager()
    print(filemanager.load("testFile"))
