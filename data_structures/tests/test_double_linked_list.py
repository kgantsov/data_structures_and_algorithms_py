import random
from unittest import TestCase

from data_structures.double_linked_list import DoubleLinkedList
from data_structures.double_linked_list import Node


class TestDoubleLinkedList(TestCase):

    def test_append(self):

        lst = DoubleLinkedList()

        expected = []
        for _ in range(50):
            x = random.randint(0, 1000000000)
            node = Node('key_{}'.format(x), 'value_{}'.format(x))
            lst.append(node)
            expected.append((node.key, node.value))

        self.assertEqual([(x.key, x.value) for x in lst], expected)
