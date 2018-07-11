import math


class BloomFilter:
    def __init__(self, probability=0.001, n=10):
        self.probability = probability

        self.size = math.ceil((n * math.log(probability)) / math.log(1 / math.pow(2,  math.log(2))))
        self.hash_table = [False] * self.size
        self.hashes_num = round(math.log(2) * self.size / n)

    def hash_func(self, key, seed=0):
        return sum(ord(x) + seed for x in str(key)) % self.size

    def add(self, key):
        for seed in range(self.hashes_num):
            self.hash_table[self.hash_func(key, seed)] = True

    def check(self, key):
        return all([
            self.hash_table[self.hash_func(key, seed)]
            for seed in range(self.hashes_num)
        ])
