
class Node:
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return '<Node key={} next={} prev={} />'.format(
            self.key,
            self.next.key if self.next else '',
            self.prev.key if self.prev else ''
        )


class DoubleLinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        self.length = 0

        lst = lst or []

        for value in lst:
            self.append(value)

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1
        return node

    def remove_node(self, node):
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is None:
            self.head = node.next

        if node.next is None:
            self.tail = node.prev

        node.prev = None
        node.next = None

        self.length -= 1
        return node

    def pop(self):
        node = self.head

        if node is None:
            return None

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is None:
            self.head = node.next

        if node.next is None:
            self.tail = node.prev

        node.prev = None
        node.next = None

        self.length -= 1
        return node

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.head

        if node is None:
            return

        while node.next is not None:
            yield node

            node = node.next

        yield node

    def __repr__(self):
        return str([x for x in self])
