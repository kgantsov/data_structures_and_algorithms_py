import random
from unittest import TestCase

from data_structures.double_linked_list import DoubleLinkedList
from data_structures.double_linked_list import Node


class TestDoubleLinkedList(TestCase):

    def test_init(self):
        lst = DoubleLinkedList()
        self.assertEqual(list(lst), [])

        lst = DoubleLinkedList([])
        self.assertEqual(list(lst), [])

        lst = DoubleLinkedList([Node('2', 2), Node('5', 5),  Node('7', 7), Node('10', 10)])
        self.assertEqual([x.key for x in lst], ['2', '5', '7', '10'])
        self.assertEqual([x.value for x in lst], [2, 5, 7, 10])

        expected_list = [
            Node('key_{}'.format(random.randint(0, 100)), random.randint(0, 100))
            for _ in range(20)
        ]

        lst = DoubleLinkedList(expected_list)
        self.assertEqual([x.key for x in lst], [x.key for x in expected_list])
        self.assertEqual([x.value for x in lst], [x.value for x in expected_list])

    def test_append(self):
        lst = DoubleLinkedList()

        expected = []
        for _ in range(50):
            x = random.randint(0, 1000000000)
            node = Node('key_{}'.format(x), 'value_{}'.format(x))
            lst.append(node)
            expected.append((node.key, node.value))

        self.assertEqual([(x.key, x.value) for x in lst], expected)

    def test_length(self):
        lst = DoubleLinkedList()
        self.assertEqual(len(lst), 0)

        lst = DoubleLinkedList([
            Node('key_{}'.format(random.randint(0, 100)), random.randint(0, 100))
            for _ in range(20)
        ])
        self.assertEqual(len(lst), 20)

        lst = DoubleLinkedList([
            Node('key_{}'.format(random.randint(0, 100)), random.randint(0, 100))
            for _ in range(48)
        ])
        self.assertEqual(len(lst), 48)

        lst = DoubleLinkedList([
            Node('key_{}'.format(random.randint(0, 100)), random.randint(0, 100))
            for _ in range(7)
        ])
        self.assertEqual(len(lst), 7)

        lst = DoubleLinkedList([
            Node('key_{}'.format(random.randint(0, 100)), random.randint(0, 100))
            for _ in range(33)
        ])
        self.assertEqual(len(lst), 33)
