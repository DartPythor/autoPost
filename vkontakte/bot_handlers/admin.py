import vkbottle.bot

import config
import vkontakte.bot_handlers.keyboard

admin_labeler = vkbottle.bot.BotLabeler()
admin_labeler.auto_rules = [
    vkbottle.bot.rules.FromPeerRule(config.ADMIN_ID),
]


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "start"}))
async def start(message: vkbottle.bot.Message, thread):
    await message.answer(
        message="Сервер запущен.",
        keyboard=vkontakte.bot_handlers.keyboard.keyboard.get_json(),
    )


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "stop"}))
async def stop(message: vkbottle.bot.Message, thread):
    await message.answer("stop")


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "start_post"}))
async def start_post(message: vkbottle.bot.Message, thread):
    await message.answer("start_post")


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "stop_post"}))
async def stop_post(message: vkbottle.bot.Message, thread):
    await message.answer("stop_post")


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "log"}))
async def log(message: vkbottle.bot.Message, thread):
    await message.answer("log")


@admin_labeler.message()
async def keyboard(message: vkbottle.bot.Message, thread):
    await message.answer(
        message="Нате",
        keyboard=vkontakte.bot_handlers.keyboard.keyboard.get_json(),
    )


__all__ = ()
