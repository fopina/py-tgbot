import json


class TGBotException(Exception):
    def __init__(self, response):
        super(TGBotException, self).__init__(response['description'], response['error_code'])
        self.response = response


class CustomKeyboard(object):
    def to_JSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
        )


class ForceReply(CustomKeyboard):
    def __init__(self, selective=False):
        self.force_reply = True

        if selective is not None:
            self.selective = selective


class ReplyKeyboardHide(CustomKeyboard):
    def __init__(self, selective=False):
        self.hide_keyboard = True

        if selective is not None:
            self.selective = selective


class ReplyKeyboardMarkup(CustomKeyboard):
    def __init__(self, options, resize_keyboard=None, one_time_keyboard=None, selective=None):
        self.keyboard = options

        if resize_keyboard is not None:
            self.resize_keyboard = resize_keyboard

        if one_time_keyboard is not None:
            self.one_time_keyboard = one_time_keyboard

        if selective is not None:
            self.selective = selective
