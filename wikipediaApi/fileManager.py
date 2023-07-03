import os


class FileManager:
    def __init__(self, pathfile: str = os.getcwd()):
        self.pathfile = pathfile

    def save(self, index_page: int, pages_list: list, plcontinue: str, filename: str) -> str:
        data_save = "\n".join((str(index_page), plcontinue, "\n".join(pages_list)))
        with open(os.path.join(self.pathfile, filename) + ".txt", mode="w", encoding="utf-8") as file:
            file.write(data_save)
        return os.path.join(self.pathfile, filename) + ".txt"

    def load(self, filename: str) -> dict:
        with open(os.path.join(self.pathfile, filename) + ".txt", mode="r", encoding="utf-8") as file:
            return {"index_page": int(file.readline()), "plcontinue": file.readline().strip(),
                    "pages_list": [i.strip() for i in file.readlines()]}


if __name__ == '__main__':
    filemanager = FileManager()
    print(filemanager.load("testFile"))
