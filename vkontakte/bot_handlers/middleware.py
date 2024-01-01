import vkbottle.bot


class ThreadInfoMiddleware(
    vkbottle.BaseMiddleware[vkbottle.bot.Message],
):
    async def pre(self):
        self.send({"thread": True})


__all__ = ()
