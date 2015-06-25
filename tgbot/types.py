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


class ReplyKeyboardHide(CustomKeyboard):
    def __init__(self, selective=False):
        self.hide_keyboard = True


class ReplyKeyboardMarkup(CustomKeyboard):
    def __init__(self, options, resize_keyboard=False, one_time_keyboard=False, selective=False):
        self.keyboard = options
