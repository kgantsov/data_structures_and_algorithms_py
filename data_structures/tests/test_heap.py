import random
from unittest import TestCase

from data_structures.heap import Heap


class TestLinkedList(TestCase):

    def test_init(self):

        tree = Heap(2, 1, 33, 5, 8, 12, 66)

        self.assertEqual(66, tree.pop())
        self.assertEqual(33, tree.pop())
        self.assertEqual(12, tree.pop())
        self.assertEqual(8, tree.pop())
        self.assertEqual(5, tree.pop())
        self.assertEqual(2, tree.pop())
        self.assertEqual(1, tree.pop())

    def test_push(self):

        tree = Heap()

        tree.push(2)
        tree.push(1)
        tree.push(33)
        tree.push(5)
        tree.push(8)
        tree.push(12)
        tree.push(66)

        self.assertEqual(66, tree.pop())
        self.assertEqual(33, tree.pop())
        self.assertEqual(12, tree.pop())
        self.assertEqual(8, tree.pop())
        self.assertEqual(5, tree.pop())
        self.assertEqual(2, tree.pop())
        self.assertEqual(1, tree.pop())
    
    def test_push(self):

        tree = Heap()

        tree.push(2)
        tree.push(1)
        tree.push(33)
        tree.push(5)
        tree.push(8)
        tree.push(12)
        tree.push(66)

        self.assertEqual(66, tree.peek())
        self.assertEqual(66, tree.peek())
        self.assertEqual(66, tree.pop())
        self.assertEqual(33, tree.peek())
        self.assertEqual(33, tree.peek())
        self.assertEqual(33, tree.pop())
        self.assertEqual(12, tree.peek())
