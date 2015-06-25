import requests
from .types import TGBotException


class TGBot(object):
    def __init__(self, token):
        self._url = 'https://api.telegram.org/bot' + token
        self._update_offset = None

    def get_me(self):
        res = requests.get(self._url + '/getMe').json()
        if res['ok']:
            return res['result']

        raise TGBotException(res)

    def get_updates(self, offset=None, limit=100, timeout=0):
        data = {
            'limit': limit,
            'timeout': timeout,
        }
        if offset is not None:
            data['offset'] = offset
        elif self._update_offset is not None:
            data['offset'] = self._update_offset

        res = requests.post(self._url + '/getUpdates', data=data).json()

        if res['ok']:
            if res['result']:
                self._update_offset = res['result'][-1]['update_id'] + 1
                return res['result']
            return []

        raise TGBotException(res)

    def send_message(self, chat_id, text, disable_web_page_preview=False, reply_to_message_id=None, reply_markup=None):
        data = {
            'chat_id': chat_id,
            'text': text,
            'disable_web_page_preview': disable_web_page_preview,
        }

        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id

        if reply_markup is not None:
            data['reply_markup'] = reply_markup.to_JSON()

        res = requests.post(self._url + '/sendMessage', data=data).json()

        if res['ok']:
            return res['result']

        raise TGBotException(res)
