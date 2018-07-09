import random
from unittest import TestCase

from data_structures.bloom_filter import BloomFilter


class TestBloomFilter(TestCase):

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
