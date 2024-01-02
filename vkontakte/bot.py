import random

import requests
import vkbottle.bot

import config
import vkontakte.bot_handlers.admin
import vkontakte.bot_handlers.middleware
import vkontakte.vk_config


class Bot(vkbottle.bot.Bot):
    def __init__(
        self,
        token=None,
        api=None,
        polling=None,
        callback=None,
        loop=None,
        loop_wrapper=None,
        router=None,
        labeler=None,
        state_dispenser=None,
        error_handler=None,
        task_each_event=True,
    ):
        super().__init__(
            token,
            api,
            polling,
            callback,
            loop,
            loop_wrapper,
            router,
            labeler,
            state_dispenser,
            error_handler,
            task_each_event,
        )
        self.token = token

    def _post(self, method, params):
        headers = {"Authorization": f"Bearer {self.token}"}
        if "v" not in params:
            params["v"] = self.api.API_VERSION

        result = requests.post(
            self.api.API_URL + method,
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

    def send_message(self, user_id, message):
        return self._post(
            "messages.send",
            {
                "user_id": user_id,
                "random_id": random.randint(1, 2_147_483_646),
                "message": message,
            },
        )

    def send_notification(self, message):
        return self.send_message(config.ADMIN_ID, message)


vkontakte.vk_config.labeler.load(vkontakte.bot_handlers.admin.admin_labeler)
vkontakte.vk_config.labeler.message_view.register_middleware(
    vkontakte.bot_handlers.middleware.ThreadInfoMiddleware,
)
bot = Bot(
    api=vkontakte.vk_config.bot_api,
    token=config.ACCESS_TOKEN_BOT,
    labeler=vkontakte.vk_config.labeler,
)

__all__ = ()
