from vkApi.apiVk import VkApiUser
from wikipediaApi.wikipediaApi import WikipediaApi
from wikipediaApi.fileManager import FileManager
import os
import schedule
import time


def start():
    path_data = os.path.join(os.getcwd(), "data")
    filemanager_start = FileManager(path_data)

    filename_start = os.path.join(path_data, "startFile.pickle")
    filename_pages = os.path.join(path_data, "pagesFile.pickle")
    if not os.path.isfile(filename_start):
        data = {"index_page": 0, "apcontinue": ""}
        filemanager_start.save(data, "startFile")
    else:
        data = filemanager_start.load("startFile")
    if not os.path.isfile(filename_pages):
        filemanager_start.save([], "pagesFile")
        data.update({"pages": []})
        data.update({"index_page": 0})
        data.update({"apcontinue": ""})
    else:
        pages = filemanager_start.load("pagesFile")
        data.update({"pages": pages})

    return data


def end(data: dict):
    path_data = os.path.join(os.getcwd(), "data")
    filemanager_start = FileManager(path_data)

    filemanager_start.save(data.pop("pages"), "pagesFile")
    filemanager_start.save(data, "startFile")


def wall_post(vk: VkApiUser, wiki: WikipediaApi, owner_id: int, data: dict) -> None:
    data_requests = wiki.get_content_page(data["pages"][data["index_page"]])
    title, data_text = list(data_requests.keys())[0], list(data_requests.values())[0]
    text = wiki.get_formate_page(title, data_text)

    data["index_page"] += 1

    vk.wall_post(owner_id, text, from_group=1)


def main(vk: VkApiUser, wiki: WikipediaApi, data: dict) -> None:
    if not data["pages"]:
        data.update(wiki.get_pages_list())
        data["index_page"] = 0

    schedule.every().day.at("09:00").do(wall_post, vk, wiki, -221307349, data)
    schedule.every().day.at("23:01").do(wall_post, vk, wiki, -221307349, data)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    access_token = input()
    user_id = 456850585
    nickname = "mr.stark3"
    vk_api = VkApiUser(access_token, user_id, nickname)
    wiki_api = WikipediaApi()

    data_save_hard_drive = start()
    try:
        main(vk_api, wiki_api, data_save_hard_drive)
    finally:
        print(data_save_hard_drive)
        end(data_save_hard_drive)
