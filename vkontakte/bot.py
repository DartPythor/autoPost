import vkontakte.vk_config
import vkbottle.bot

import vkontakte.bot_handlers.admin
import vkontakte.bot_handlers.middleware


vkontakte.vk_config.labeler.load(vkontakte.bot_handlers.admin.admin_labeler)
vkontakte.vk_config.labeler.message_view.register_middleware(
    vkontakte.bot_handlers.middleware.ThreadInfoMiddleware,
)
bot = vkbottle.bot.Bot(
    api=vkontakte.vk_config.bot_api,
    labeler=vkontakte.vk_config.labeler,
)
