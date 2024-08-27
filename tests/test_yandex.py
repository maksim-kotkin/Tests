import unittest
from yandex import auth_yandex

def test_summarize_1(login, password):
    login = ''
    password = ''
    expected = "https://passport.yandex.ru/auth/challenge?retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fprepare%3Fuuid%3D57ebd472-1d5c-44c2-a5a4-195f8e321db0%26goal%3Dhttps%253A%252F%252Fya.ru%252F%26finish%3Dhttps%253A%252F%252Fpassport.yandex.ru%252Fprofile&track_id=f8616b146b0fa432bc50fd32aa60ee659b"
    actual = auth_yandex(login, password)
    self.assertEqual(expected, actual)