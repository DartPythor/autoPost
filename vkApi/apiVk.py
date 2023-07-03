if __name__ != '__main__':
    from vkApi.interfaceVkApi import InterfaceVkApi
else:
    from interfaceVkApi import InterfaceVkApi

import requests
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
handler = logging.FileHandler("VkApi.log", mode="w")
format_handler = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(format_handler)
logger.addHandler(handler)


class VkApiUser(InterfaceVkApi):
    http = "https://api.vk.com/method/"

    def __init__(self, token: str, user_id: int = None, nickname: str = None):
        self.token = token
        self.user_id = user_id
        self.nickname = nickname

        self.api_version = 5.131
        self.wait = 25

    def _post(self, method: str, params: dict):
        headers = {"Authorization": f"Bearer {self.token}"}
        if "v" not in params: params["v"] = self.api_version
        logger.debug(f"send post requests: {method}, params: {params}")
        logger.info(f"send post requests: {method}, params: {params}")

        result = requests.post(self.http + method, params=params, headers=headers).json()

        logger.debug(f"result request: {result}")
        logger.info(f"result request: {result}")
        if "error" in result:
            if result["error"]["error_code"] == 5:
                logger.critical(f"Access_token invalid: {result['error']}")
                raise Exception(f"Access_token invalid: {result['error']}")

            elif result["error"]["error_code"] == 100:
                logger.error(f"Params invalid: {result['error']}")
                raise Exception(f"Params invalid: {result['error']}")

            logger.error(f"Unknown error, {result['error']}")
            raise Exception(f"Unknown error, {result['error']}")
        return result["response"]

    def wall_post(self, owner_id: int, text: str | None, **kwargs):
        kwargs.update({"owner_id": owner_id})
        kwargs.update({"message": text})
        return self._post("wall.post", kwargs)


if __name__ == '__main__':
    access_token = "vk1.a.vH9qoivRrVEZc4mp10Jla0P_cZb4FNo3d-h9x4ilxHaI8EbAsylfkPot3bfdVsuoq0r2sIlcgOA0Qos4F3E9HHRctbn6WgUgEiGaAV_KkfP-b2bE3PdpE-nWVDiQrgDxQOKJ4tly2GvoZi-zxusYsHbAxPZ6hpIA9MlpiuvStCtYZspSvFBUC-q1RDooyC0kVzCwOJPiCwBhY2TAwgoOwg"
    user_id = 456850585
    nickname = "mr.stark3"
    vk = VkApiUser(access_token, user_id, nickname)
    vk.wall_post(-221307349, "Hello guys, test message :> again", from_group=1)
