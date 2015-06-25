import requests
import json


class TGBot(object):
    def __init__(self, token):
        self._url = 'https://api.telegram.org/bot' + token
        self._update_offset = None

    def get_me(self):
        res = json.loads(requests.get(self._url + '/getMe').content)
        if res['ok']:
            return res['result']

        raise Exception('Unknown error', res)

    def get_updates(self, offset=None, limit=100, timeout=0):
        data = {
            'limit': limit,
            'timeout': timeout,
        }
        if offset is not None:
            data['offset'] = offset
        elif self._update_offset is not None:
            data['offset'] = self._update_offset

        res = json.loads(requests.post(self._url + '/getUpdates', data=data).content)

        if res['ok']:
            if res['result']:
                self._update_offset = res['result'][-1]['update_id'] + 1
                return res['result']
            return []

        raise Exception('Unknown error', res)
