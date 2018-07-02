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

    def test_get(self):
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

    def test_capacity(self):
        m = HashMap()

        self.assertEqual(None, m.get('test'))

        m.set('my_key_1', 'my value 1')
        self.assertEqual(2, m.capacity)
        m.set('my_key_2', 'my value 2')
        self.assertEqual(2, m.capacity)
        m.set('my_key_3', 'my value 3')
        self.assertEqual(4, m.capacity)
        m.set('my_key_4', 'my value 4')
        self.assertEqual(8, m.capacity)
        m.set('my_key_5', 'my value 5')
        self.assertEqual(8, m.capacity)
        m.set('my_key_6', 'my value 6')
        self.assertEqual(16, m.capacity)
        m.set('my_key_7', 'my value 7')
        self.assertEqual(16, m.capacity)
        m.set('my_key_8', 'my value 8')
        self.assertEqual(16, m.capacity)
        m.set('my_key_9', 'my value 9')
        self.assertEqual(16, m.capacity)
        m.set('my_key_10', 'my value 10')
        self.assertEqual(32, m.capacity)
        m.set('my_key_11', 'my value 11')
        self.assertEqual(32, m.capacity)

        m.delete('my_key_11')
        self.assertEqual(32, m.capacity)
        m.delete('my_key_10')
        self.assertEqual(32, m.capacity)
        m.delete('my_key_9')
        self.assertEqual(32, m.capacity)
        m.delete('my_key_8')
        self.assertEqual(32, m.capacity)
        m.delete('my_key_8')
        self.assertEqual(16, m.capacity)
        m.delete('my_key_7')
        self.assertEqual(16, m.capacity)
        m.delete('my_key_6')
        self.assertEqual(16, m.capacity)
        m.delete('my_key_5')
        self.assertEqual(16, m.capacity)
        m.delete('my_key_4')
        self.assertEqual(16, m.capacity)
        m.delete('my_key_3')
        self.assertEqual(8, m.capacity)
        m.delete('my_key_2')
        self.assertEqual(8, m.capacity)
        m.delete('my_key_1')
        self.assertEqual(4, m.capacity)

    def test_keys(self):
        m = HashMap()
        for x in range(30):
            key = 'my_key_{}'.format(x)
            value = 'my value {}'.format(x)

            m.set(key, value)

        self.assertEqual(30, len(list(m.keys())))
        self.assertEqual(set('my_key_{}'.format(x) for x in range(30)), set(m.keys()))

    def test_values(self):
        m = HashMap()
        for x in range(30):
            key = 'my_key_{}'.format(x)
            value = 'my value {}'.format(x)

            m.set(key, value)

        self.assertEqual(30, len(list(m.values())))
        self.assertEqual(set('my value {}'.format(x) for x in range(30)), set(m.values()))

    def test_items(self):
        m = HashMap()
        for x in range(30):
            key = 'my_key_{}'.format(x)
            value = 'my value {}'.format(x)

            m.set(key, value)

        self.assertEqual(30, len(list(m.items())))
        self.assertEqual(
            set(('my_key_{}'.format(x), 'my value {}'.format(x)) for x in range(30)),
            set(m.items())
        )

    def test_magic_methods(self):
        m = HashMap()

        m['key_1'] = 'value 1'
        m['key_2'] = 'value 2'
        m['key_3'] = 'value 3'

        self.assertEqual(m['key_1'], 'value 1')
        self.assertEqual(m['key_2'], 'value 2')
        self.assertEqual(m['key_3'], 'value 3')

        del m['key_1']
        self.assertEqual(m['key_1'], None)
        self.assertEqual(m['key_2'], 'value 2')
        self.assertEqual(m['key_3'], 'value 3')

        del m['key_2']
        del m['key_3']

        self.assertEqual(m['key_1'], None)
        self.assertEqual(m['key_2'], None)
        self.assertEqual(m['key_3'], None)

    def test_iterator(self):
        m = HashMap()

        m['key_1'] = 'value 1'
        m['key_2'] = 'value 2'
        m['key_3'] = 'value 3'

        self.assertEqual({'key_1', 'key_2', 'key_3'}, {k for k, _ in m})
        self.assertEqual({'value 1', 'value 2', 'value 3'}, {v for _, v in m})

    def test_contains(self):
        m = HashMap()

        m['key_1'] = 'value 1'
        m['key_2'] = 'value 2'
        m['key_3'] = 'value 3'

        self.assertEqual(True, 'key_1' in m)
        self.assertEqual(True, 'key_2' in m)
        self.assertEqual(True, 'key_3' in m)
        self.assertEqual(False, 'key_4' in m)
        self.assertEqual(False, 'key_5' in m)
        self.assertEqual(False, 'key_6' in m)

    def test_len(self):
        m = HashMap()

        self.assertEqual(0, len(m))

        for x in range(30):
            key = 'my_key_{}'.format(x)
            value = 'my value {}'.format(x)

            m.set(key, value)

            self.assertEqual(x + 1, len(m))
