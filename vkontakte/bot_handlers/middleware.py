import vkbottle.bot


class ThreadInfoMiddleware(
    vkbottle.BaseMiddleware[vkbottle.bot.Message],
):
    thread = None

    async def pre(self):
        self.send({"thread": self.get_thread()})

    @staticmethod
    def set_thread(thread):
        ThreadInfoMiddleware.thread = thread

    def get_thread(self):
        return self.thread


__all__ = ()
