import random
from unittest import TestCase

from data_structures.bloom_filter import BloomFilter


class TestBloomFilter(TestCase):

    def test_size(self):
        b = BloomFilter(probability=0.1, capacity=2)
        self.assertEqual(len(b.hash_table), 10)

        self.assertEqual(len(b), 2)

        b = BloomFilter(probability=0.1, capacity=5)
        self.assertEqual(len(b.hash_table), 24)

        self.assertEqual(len(b), 5)

        b = BloomFilter(probability=0.1, capacity=10)
        self.assertEqual(len(b.hash_table), 48)

        self.assertEqual(len(b), 10)

        b = BloomFilter(probability=0.1, capacity=100)
        self.assertEqual(len(b.hash_table), 480)
        
        self.assertEqual(len(b), 100)

        b = BloomFilter(probability=0.1, capacity=1000)
        self.assertEqual(len(b.hash_table), 4793)

        self.assertEqual(len(b), 1000)

        b = BloomFilter(probability=0.01, capacity=2)
        self.assertEqual(len(b.hash_table), 20)

        self.assertEqual(len(b), 2)

        b = BloomFilter(probability=0.01, capacity=5)
        self.assertEqual(len(b.hash_table), 48)

        self.assertEqual(len(b), 5)

        b = BloomFilter(probability=0.01, capacity=10)
        self.assertEqual(len(b.hash_table), 96)

        self.assertEqual(len(b), 10)

        b = BloomFilter(probability=0.01, capacity=100)
        self.assertEqual(len(b.hash_table), 959)

        self.assertEqual(len(b), 100)

        b = BloomFilter(probability=0.01, capacity=1000)
        self.assertEqual(len(b.hash_table), 9586)

        self.assertEqual(len(b), 1000)

        b = BloomFilter(probability=0.0005, capacity=2)
        self.assertEqual(len(b.hash_table), 32)

        self.assertEqual(len(b), 2)

        b = BloomFilter(probability=0.0005, capacity=5)
        self.assertEqual(len(b.hash_table), 80)

        self.assertEqual(len(b), 5)

        b = BloomFilter(probability=0.0005, capacity=10)
        self.assertEqual(len(b.hash_table), 159)

        self.assertEqual(len(b), 10)

        b = BloomFilter(probability=0.0005, capacity=100)
        self.assertEqual(len(b.hash_table), 1583)

        self.assertEqual(len(b), 100)

        b = BloomFilter(probability=0.0005, capacity=1000)
        self.assertEqual(len(b.hash_table), 15821)

        self.assertEqual(len(b), 1000)

        b = BloomFilter(probability=0.0005, capacity=5000)
        self.assertEqual(len(b.hash_table), 79102)

        self.assertEqual(len(b), 5000)

    def test_set(self):
        b = BloomFilter()

        self.assertFalse(b.check("user:35"))
        self.assertFalse(b.check("user:165"))
        self.assertFalse(b.check("user:55"))
        self.assertFalse(b.check("user:99"))

        b.add("user:35")

        self.assertTrue(b.check("user:35"))
        self.assertFalse(b.check("user:165"))
        self.assertFalse(b.check("user:55"))
        self.assertFalse(b.check("user:99"))

        b.add("user:165")
        self.assertTrue(b.check("user:35"))
        self.assertTrue(b.check("user:165"))
        self.assertFalse(b.check("user:55"))
        self.assertFalse(b.check("user:99"))
        b.add("user:55")
        b.add("user:99")
        self.assertTrue(b.check("user:55"))
        self.assertTrue(b.check("user:99"))
