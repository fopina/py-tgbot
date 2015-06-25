import unittest
from tgbot import TGBot
from requests.packages import urllib3
urllib3.disable_warnings()

TELEGRAM_KEY = ''


class TGBotTest(unittest.TestCase):
    def test_getMe(self):
        tg = TGBot(TELEGRAM_KEY)
        res = tg.get_me()
        self.assertTrue(res['ok'])

if __name__ == '__main__':
    unittest.main()
