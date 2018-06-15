
class Heap(object):
    def __init__(self, *args):
        self.nodes = [0]
        self.size = 0

        for item in args:
            self.push(item)

    def __repr__(self):
        return self.nodes[1:]

    def move_up(self, size):
        while size // 2 > 0:
            if self.nodes[size] > self.nodes[size // 2]:
                self.nodes[size], self.nodes[size // 2] = self.nodes[size // 2], self.nodes[size]

            size //= 2

    def max_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.nodes[index * 2] > self.nodes[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def move_down(self, index):
        while index * 2 <= self.size:
            max_child = self.max_child(index)

            if self.nodes[index] < self.nodes[max_child]:
                self.nodes[index], self.nodes[max_child] = self.nodes[max_child], self.nodes[index]

            index = max_child

    def push(self, item):
        self.nodes.append(item)
        self.size += 1
        self.move_up(self.size)

    def pop(self):
        val = self.nodes[1]
        self.nodes[1] = self.nodes[self.size]
        self.size -= 1
        self.nodes.pop()
        self.move_down(1)

        return val

    def peek(self):
        return self.nodes[1]
