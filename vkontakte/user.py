import requests

import config


class User:
    http = "https://api.vk.com/method/"

    def __init__(self, token: str, user_id: int = None, nickname: str = None):
        self.token = token
        self.user_id = user_id
        self.nickname = nickname

        self.api_version = 5.131
        self.wait = 25

    def _post(self, method: str, params: dict):
        headers = {"Authorization": f"Bearer {self.token}"}
        if "v" not in params:
            params["v"] = self.api_version

        result = requests.post(
            self.http + method,
            params=params,
            headers=headers,
        ).json()

        if "error" in result:
            if result["error"]["error_code"] == 5:
                raise Exception(f"Access_token invalid: {result['error']}")

            elif result["error"]["error_code"] == 100:
                raise Exception(f"Params invalid: {result['error']}")

            raise Exception(f"Unknown error, {result['error']}")
        return result["response"]

    def wall_post(self, owner_id: int, text: str | None, from_group=1, **kwargs):
        kwargs.update({"owner_id": owner_id})
        kwargs.update({"message": text})
        kwargs.update({"from_group": from_group})
        return self._post("wall.post", kwargs)


user = User(config.ACCESS_TOKEN_USER, config.ADMIN_ID)

__all__ = ()
