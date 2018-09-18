import random
from unittest import TestCase

from data_structures.lru_cache import LRUCache


class TestLRUCache(TestCase):

    # def test_init(self):
    #     lst = LRUCache()
    #     self.assertEqual(list(lst), [])

    #     lst = LRUCache([])
    #     self.assertEqual(list(lst), [])

    #     lst = LRUCache([2, 5,  7, 10])
    #     self.assertEqual(list(lst), [2, 5, 7, 10])

    #     expected_list = [random.randint(0, 100) for _ in range(20)]
    #     lst = LRUCache(expected_list)
    #     self.assertEqual(list(lst), expected_list)

    def test_set(self):
        cache = LRUCache(capacity=4)

        for n in range(10):
            key, value = 'key_{}'.format(n), 'value_{}'.format(n)
            cache.set(key, value)

            self.assertEqual(cache.get(key), value)

        for n in range(4):
            key, value = 'key_{}'.format(n), 'value_{}'.format(n)
            self.assertEqual(cache.get('key_1'), None)

        for n in range(4, 10):
            key, value = 'key_{}'.format(n), 'value_{}'.format(n)
            self.assertEqual(cache.get('key_1'), None)

    def test_get(self):
        cache = LRUCache(capacity=4)

        for n in range(10):
            key, value = 'key_{}'.format(n), 'value_{}'.format(n)
            cache.set(key, value)

            self.assertEqual(cache.get(key), value)

        cache.get('key_8')
        cache.get('key_7')
        cache.get('key_8')

        cache.set('key_55', 'value_55')
        cache.set('key_76', 'value_76')

        self.assertEqual(cache.get('key_7'), 'value_7')
        self.assertEqual(cache.get('key_8'), 'value_8')
        self.assertEqual(cache.get('key_55'), 'value_55')
        self.assertEqual(cache.get('key_76'), 'value_76')
