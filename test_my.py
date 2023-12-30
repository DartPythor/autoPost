import time

import schedule
import threading
import asyncio


class Thread(threading.Thread):
    def run(self):
        while True:
            time.sleep(1)
            schedule.run_pending()


class Bot:
    async def message(self):
        while True:
            await asyncio.sleep(3)
            print(f"BOT MESSAGE {self}")

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.message())


schedule.every().second.do(lambda: print("1"))
sender = Thread()
sender.start()

bot = Bot()
bot.run()
