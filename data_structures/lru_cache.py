from data_structures.double_linked_list import Node
from data_structures.double_linked_list import DoubleLinkedList


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = DoubleLinkedList()

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.queue.remove_node(node)
            self.queue.append(node)
            return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.queue.remove_node(node)
            self.queue.append(node)
        else:
            if len(self.queue) >= self.capacity:
                node = self.queue.pop()
                del self.cache[node.key]

            node = Node(key, value)
            self.queue.append(node)
            self.cache[key] = node

    def delete(self, key):
        if key in self.cache:
            node = self.cache[key]

            self.queue.remove_node(node)

            del self.cache[key]
