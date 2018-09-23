import random
import time
from unittest import TestCase

from data_structures.rate_limiter import RateLimiter


class TestRateLimiter(TestCase):

    def test_slow(self):

        rl = RateLimiter()
        rl.add('login', 5, 2, 5)

        self.assertEqual(rl.reduce('login', 1), 4)
        self.assertEqual(rl.reduce('login', 1), 3)
        self.assertEqual(rl.reduce('login', 1), 2)
        self.assertEqual(rl.reduce('login', 1), 1)
        self.assertEqual(rl.reduce('login', 1), False)
        time.sleep(2)

        self.assertEqual(rl.reduce('login', 1), 4)
        self.assertEqual(rl.reduce('login', 1), 3)
        self.assertEqual(rl.reduce('login', 1), 2)
        self.assertEqual(rl.reduce('login', 1), 1)
        self.assertEqual(rl.reduce('login', 1), False)
        time.sleep(2)

        self.assertEqual(rl.reduce('login', 1), 4)

    def test_fast(self):
        rl = RateLimiter()
        rl.add('api_call', 1000, 1, 1000)

        for x in range(999, 0, -1):
            self.assertEqual(rl.reduce('api_call', 1), x)
        self.assertEqual(rl.reduce('api_call', 1), False)
        time.sleep(1)

        for x in range(999, 0, -1):
            self.assertEqual(rl.reduce('api_call', 1), x)
        self.assertEqual(rl.reduce('api_call', 1), False)
