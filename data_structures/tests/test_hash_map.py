import random
from unittest import TestCase

from data_structures.hash_map import HashMap


class TestLinkedList(TestCase):

    def test_set(self):
        m = HashMap()
        for x in range(30):
            key = 'my_key_{}'.format(x)
            value = 'my value {}'.format(x)

            m.set(key, value)

        for x in range(30):
            key = 'my_key_{}'.format(x)
            value = 'my value {}'.format(x)

            self.assertEqual(value, m.get(key))
