from collections import deque


# Dumb solution:
class ZigZagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
        self.v1 = v1
        self.v2 = v2
        self.counter_1 = self.counter_2 = 0
        self.current = 0

    def next(self) -> int:
        if self.counter_1 == len(self.v1):
            if self.counter_2 == len(self.v2):
                raise StopIteration()
            self.counter_2 += 1
            return self.v2[self.counter_2 - 1]

        if self.counter_2 == len(self.v2):
            if self.counter_1 == len(self.v1):
                raise StopIteration()
            self.counter_1 += 1
            return self.v1[self.counter_1 - 1]

        if self.current == 0:
            self.counter_1 += 1
            self.current = 1
            return self.v1[self.counter_1 - 1]
        else:
            self.counter_2 += 1
            self.current = 0
            return self.v2[self.counter_2 - 1]

#
# v1 = [1, 2, 3]
# v2 = [444]
# Z = ZigZagIterator(v1, v2)
# v = []
# for i in range(len(v1) + len(v2)):
#     v.append(Z.next())
# print(v)


# Smart solution
class KZigZagIterator:
    def __init__(self, vectors: list[list[int]]):
        self.vectors = vectors
        self.deque = deque()
        for i in range(len(vectors)):
            if len(vectors[i]):
                self.deque.append((i, 0, len(vectors[i])))

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration()

        index, start, end = self.deque.popleft()
        if start + 1 < end:
            self.deque.append((index, start + 1, end))
        return self.vectors[index][start]

    def hasNext(self):
        return len(self.deque) != 0


v1 = [1, 2, 3]
v2 = [111, 112]
v3 = []
v4 = [15, 16, 17, 18, 19, 20]
length = len(v1) + len(v2) + len(v3) + len(v4)
Z = KZigZagIterator([v1, v2, v3, v4])
v = []
for i in range(length):
    v.append(Z.next())
print(v)









