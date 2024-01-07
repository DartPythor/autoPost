import config
import poster.poster_thread
import vkontakte.bot
import vkontakte.bot_handlers.middleware


thread_post = poster.poster_thread.PosterThread(
    config.DAY_POST,
    config.NIGHT_POST,
    config.TIMEZONE,
)
thread_post.start()
vkontakte.bot_handlers.middleware.ThreadInfoMiddleware.set_thread(thread_post)
vkontakte.bot.bot.run_forever()
