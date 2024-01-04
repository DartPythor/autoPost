import vkbottle.bot

import config
import vkontakte.bot_handlers.keyboard

admin_labeler = vkbottle.bot.BotLabeler()
admin_labeler.auto_rules = [
    vkbottle.bot.rules.FromPeerRule(config.ADMIN_ID),
]


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "start"}))
async def start(message: vkbottle.bot.Message, thread):
    server_log = f"Состояние сервера: {thread.is_alive()}"
    server_log += "✅" if thread.is_alive() else "❌"

    poster_log = f"Состояние постера: {thread.is_stop()}"
    poster_log += "✅" if thread.is_stop() else "❌"

    all_log = "\n".join(
        (
            server_log,
            poster_log,
        ),
    )
    await message.answer(
        message=all_log,
        keyboard=vkontakte.bot_handlers.keyboard.keyboard.get_json(),
    )


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "stop"}))
async def stop(message: vkbottle.bot.Message, thread):
    thread.stop()
    await message.answer(
        message="Сервер отключен ❌",
        keyboard=vkbottle.EMPTY_KEYBOARD,
    )
    exit(0)


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "start_post"}))
async def start_post(message: vkbottle.bot.Message, thread):
    thread.start_post()
    await message.answer("Постинг включен ✅")


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "stop_post"}))
async def stop_post(message: vkbottle.bot.Message, thread):
    thread.stop_post()
    await message.answer("Постинг выключен ❌")


@admin_labeler.message(vkbottle.bot.rules.PayloadRule({"command": "log"}))
async def log(message: vkbottle.bot.Message, thread):
    thread_log = "\n"
    thread_log = thread_log.join(
        (
            f"Состояние сервера: {thread.is_alive()}",
            f"Состояние постера: {thread.is_stop()}",
            f"Временная зона: {thread.timezone}",
            f"Время постинга днем: {thread.day_post}",
            f"Время постинга вечером: {thread.night_post}",
        ),
    )
    await message.answer(message=thread_log)


@admin_labeler.message()
async def keyboard(message: vkbottle.bot.Message, thread):
    await message.answer(
        message=f"Обновление клавиатуры\nСостояние сервера: {thread.is_alive()}",
        keyboard=vkontakte.bot_handlers.keyboard.keyboard.get_json(),
    )


__all__ = ()
