

class HashMap:
    def __init__(self):
        self.capacity = 2
        self.size = 0

        self.hash_table = [[] for i in range(self.capacity)]

    def set(self, key, value):
        if self._load() > 0.5:
            self._resize(self.capacity * 2)

        index = hash(key) % self.capacity
        self.hash_table[index].append((key, value))
        self.size += 1

    def get(self, key):
        index = hash(key) % self.capacity

        if not self.hash_table[index]:
            return None
        else:
            return next((v for k, v in self.hash_table[index] if k == key), None)

    def delete(self, key):
        if self._load() < 0.25:
            self._resize(self.capacity // 2)

        index = hash(key) % self.capacity
        if not self.hash_table[index]:
            return None
        else:
            sub_index = next((i for i, x in enumerate(self.hash_table[index]) if x[0] == key), None)
            del self.hash_table[index][sub_index]
            self.size -= 1

    def keys(self):
        for bucket in self.hash_table:
            for key, _ in bucket:
                yield key

    def values(self):
        for bucket in self.hash_table:
            for _, value in bucket:
                yield value

    def _resize(self, capacity):
        hash_table = [[] for i in range(capacity)]

        for bucket in self.hash_table:
            for key, value in bucket:
                index = hash(key) % capacity
                hash_table[index].append((key, value))

        self.hash_table = hash_table
        self.capacity = capacity

    def _load(self):
        return float(self.size) / float(self.capacity)
