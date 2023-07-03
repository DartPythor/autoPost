from vkApi.apiVk import VkApiUser
from wikipediaApi.wikipediaApi import WikipediaApi


def main(vk: VkApiUser, wiki: WikipediaApi) -> None:
    ...


if __name__ == '__main__':
    access_token = "vk1.a.vH9qoivRrVEZc4mp10Jla0P_cZb4FNo3d-h9x4ilxHaI8EbAsylfkPot3bfdVsuoq0r2sIlcgOA0Qos4F3E9HHRctbn6WgUgEiGaAV_KkfP-b2bE3PdpE-nWVDiQrgDxQOKJ4tly2GvoZi-zxusYsHbAxPZ6hpIA9MlpiuvStCtYZspSvFBUC-q1RDooyC0kVzCwOJPiCwBhY2TAwgoOwg"
    user_id = 456850585
    nickname = "mr.stark3"
    vk_api = VkApiUser(access_token, user_id, nickname)
    wiki_api = WikipediaApi()
    data_save_hard_drive = {}
    main(vk_api, wiki_api)
