import vk_config
import vkbottle.bot

import vkontakte.bot_handlers.admin
import vkontakte.bot_handlers.middleware


vk_config.labeler.load(vkontakte.bot_handlers.admin.admin_labeler)
vk_config.labeler.message_view.register_middleware(
    vkontakte.bot_handlers.middleware.ThreadInfoMiddleware,
)
bot = vkbottle.bot.Bot(
    api=vk_config.bot_api,
    labeler=vk_config.labeler,
)
