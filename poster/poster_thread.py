import threading
import time
import schedule

import config
import chatGPT.chat_gpt
import vkontakte.bot
import vkontakte.user
import wikipedia.wikipedia_api


class PosterThread(threading.Thread):
    def __init__(
        self,
        day_post,
        night_post,
        timezone,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.day_post = day_post
        self.night_post = night_post
        self.timezone = timezone

        self.wikipedia = wikipedia.wikipedia_api.WikipediaApi()
        self.user = vkontakte.user.user
        self.bot = vkontakte.bot.bot
        self.chat_gpt = chatGPT.chat_gpt.ChatGPT()

        self._stop_event = threading.Event()

    def run(self):
        self.set_schedule(self.send_post)
        self.bot.send_notification("Thread poster run!")
        while True:
            self._stop_event.wait()
            time.sleep(10)
            schedule.run_pending()

    def set_schedule(self, func):
        for t in self.day_post, self.night_post:
            schedule.every().day.at(t).do(func)

    def get_title(self):
        return self.wikipedia.get_title()

    def send_post(self):
        try:
            theme = self.get_title()
            text = self.get_post_content(theme)
            self.user.wall_post(config.GROUP_ID, text)
        except Exception as error:
            self.bot.send_notification(f"Error send post!\nError: {error}")
            self.wikipedia.set_backup()
        else:
            self.send_notification(theme)

    def send_notification(self, theme):
        return self.bot.send_notification(f"Пост выложен на тему: {theme}")

    def get_post_content(self, theme):
        return self.chat_gpt.make_post_content(theme)

    def stop(self):
        self._stop_event.set()

    def start_post(self):
        self._stop_event.clear()

    def is_stop(self):
        self._stop_event.is_set()
