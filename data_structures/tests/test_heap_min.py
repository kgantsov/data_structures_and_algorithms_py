import random
from unittest import TestCase

from data_structures.heap_min import HeapMin


class TestLinkedList(TestCase):

    def test_init(self):
        tree = HeapMin(2, 1, 33, 5, 8, 12, 66)

        self.assertEqual(1, tree.pop())
        self.assertEqual(2, tree.pop())
        self.assertEqual(5, tree.pop())
        self.assertEqual(8, tree.pop())
        self.assertEqual(12, tree.pop())
        self.assertEqual(33, tree.pop())
        self.assertEqual(66, tree.pop())

    def test_push(self):
        tree = HeapMin()

        tree.push(2)
        tree.push(1)
        tree.push(33)
        tree.push(5)
        tree.push(8)
        tree.push(12)
        tree.push(66)

        self.assertEqual(1, tree.pop())
        self.assertEqual(2, tree.pop())
        self.assertEqual(5, tree.pop())
        self.assertEqual(8, tree.pop())
        self.assertEqual(12, tree.pop())
        self.assertEqual(33, tree.pop())
        self.assertEqual(66, tree.pop())

    def test_peek(self):
        tree = HeapMin()

        tree.push(2)
        tree.push(1)
        tree.push(33)
        tree.push(5)
        tree.push(8)
        tree.push(12)
        tree.push(66)

        self.assertEqual(1, tree.peek())
        self.assertEqual(1, tree.peek())
        self.assertEqual(1, tree.pop())
        self.assertEqual(2, tree.peek())
        self.assertEqual(2, tree.peek())
        self.assertEqual(2, tree.pop())
        self.assertEqual(5, tree.peek())

    def test_len(self):
        tree = HeapMin()

        tree.push(2)
        self.assertEqual(1, len(tree))
        tree.push(1)
        self.assertEqual(2, len(tree))
        tree.push(33)
        self.assertEqual(3, len(tree))
        tree.push(5)
        self.assertEqual(4, len(tree))
        tree.push(8)
        self.assertEqual(5, len(tree))
        tree.push(12)
        self.assertEqual(6, len(tree))
        tree.push(66)
        self.assertEqual(7, len(tree))

        tree.pop()
        self.assertEqual(6, len(tree))
        tree.pop()
        self.assertEqual(5, len(tree))
        tree.pop()
        self.assertEqual(4, len(tree))
        tree.pop()
        self.assertEqual(3, len(tree))
        tree.pop()
        self.assertEqual(2, len(tree))
        tree.pop()
        self.assertEqual(1, len(tree))
        tree.pop()
        self.assertEqual(0, len(tree))
