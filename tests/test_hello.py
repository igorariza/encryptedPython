import unittest

from encrypted.hello import hello


class HelloTestCase(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(
            hello(),
            'Hello world!'
        )