
class HeapMin(object):
    def __init__(self, *args):
        self.nodes = [0]
        self.size = 0

        for item in args:
            self.push(item)

    def __len__(self):
        return self.size

    def __repr__(self):
        return self.nodes[1:]

    def move_up(self, size):
        while size // 2 > 0:
            if self.nodes[size] < self.nodes[size // 2]:
                self.nodes[size], self.nodes[size // 2] = self.nodes[size // 2], self.nodes[size]

            size //= 2

    def min_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.nodes[index * 2] < self.nodes[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def move_down(self, index):
        while index * 2 <= self.size:
            min_child = self.min_child(index)

            if self.nodes[index] > self.nodes[min_child]:
                self.nodes[index], self.nodes[min_child] = self.nodes[min_child], self.nodes[index]

            index = min_child

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
