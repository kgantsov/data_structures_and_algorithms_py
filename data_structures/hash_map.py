

class HashMap:
    def __init__(self):
        self.capacity = 10
        self.size = 0

        self.hash_table = [[] for i in range(self.capacity)]

    def set(self, key, value):
        index = hash(key) % self.capacity
        self.hash_table[index].append((key, value))

    def get(self, key):
        index = hash(key) % self.capacity

        if not self.hash_table[index]:
            return None
        else:
            return next((v for k, v in self.hash_table[index] if k == key), None)

    def delete(self, key):
        index = hash(key) % self.capacity
        if not self.hash_table[index]:
            return None
        else:
            sub_index = next((i for i, x in enumerate(self.hash_table[index]) if x[0] == key), None)
            del self.hash_table[index][sub_index]