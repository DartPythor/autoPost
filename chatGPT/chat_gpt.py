import os.path

import g4f

import config


class ChatGPT(g4f.ChatCompletion):
    def __init__(
        self,
        model=g4f.models.gpt_4,
        role="user",
        filename="chatGPT_message.txt",
    ):
        self.model = model
        self.role = role
        self.filename = filename

    def get_template(self, theme, content):
        with open(
            os.path.join(
                config.FILE_STORAGE_TEMPLATES,
                self.filename,
            ),
            mode="r",
            encoding="utf-8",
        ) as file:
            template = file.readline()
        return template.format(theme=theme, content=content)

    def make_post_content(self, theme, content):
        return self.create(
            model=self.model,
            messages=[
                {"role": self.role, "content": self.get_template(theme, content)},
            ],
        )


__all__ = ()
