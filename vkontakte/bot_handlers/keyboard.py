import vkbottle

KEYBOARD_TEXT = {
    "star_post_button": "Начать постинг",
    "stop_post_button": "Остановить постинг",
    "log_button": "Журнал",
    "stop_button": "Остановить бота",
}


class Keyboard(vkbottle.Keyboard):
    def __init__(self, one_time=False, inline=False):
        super().__init__(one_time, inline)
        self.set_keyboard()

    def set_keyboard(self):
        self.add(
            vkbottle.Text(
                KEYBOARD_TEXT["star_post_button"],
                payload={"command": "start_post"},
            ),
            vkbottle.KeyboardButtonColor.POSITIVE,
        )
        self.add(
            vkbottle.Text(
                KEYBOARD_TEXT["stop_post_button"],
                payload={"command": "stop_post"},
            ),
            vkbottle.KeyboardButtonColor.NEGATIVE,
        )
        self.row()
        self.add(
            vkbottle.Text(
                KEYBOARD_TEXT["log_button"],
                payload={"command": "log"},
            ),
            vkbottle.KeyboardButtonColor.PRIMARY,
        )
        self.add(
            vkbottle.Text(
                KEYBOARD_TEXT["stop_button"],
                payload={"command": "stop"},
            ),
            vkbottle.KeyboardButtonColor.NEGATIVE,
        )


keyboard = Keyboard()

__all__ = ()
