import random
from unittest import TestCase

from data_structures.hash_map import HashMap


class TestLinkedList(TestCase):

    def test_get(self):
        m = HashMap()
        for x in range(30):
            key = 'my_key_{}'.format(x)
            value = 'my value {}'.format(x)

            m.set(key, value)

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

    def test_delete(self):
        m = HashMap()

        self.assertEqual(None, m.get('test'))

        for x in range(30):
            key = 'my_key_{}'.format(x)
            value = 'my value {}'.format(x)

            m.set(key, value)

        for x in range(30):
            key = 'my_key_{}'.format(x)
            value = 'my value {}'.format(x)

            self.assertEqual(value, m.get(key))

        m.delete('my_key_2')
        m.delete('my_key_7')
        m.delete('my_key_10')
        m.delete('my_key_18')
        m.delete('my_key_20')

        self.assertEqual(None, m.get('my_key_2'))
        self.assertEqual(None, m.get('my_key_7'))
        self.assertEqual(None, m.get('my_key_10'))
        self.assertEqual(None, m.get('my_key_18'))
        self.assertEqual(None, m.get('my_key_20'))
