from collections import OrderedDict as Od, defaultdict
from lib2to3.pytree import Node


# Lazy solution using OrderedDict
class LRUCacheLazy:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.data: dict[int, int] = Od()

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        value = self.data.pop(key)
        self.data[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            if len(self.data) == self.capacity:
                self.data.popitem(last=False)
            self.data[key] = value
        else:
            self.data[key] = value
            self.data[key] = self.data.pop(key)


# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)
# lRUCache.put(2, 2)
# print(lRUCache.get(1))
# lRUCache.put(3, 3)
# print(lRUCache.get(2))
# lRUCache.put(4, 4)
# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))

# Normal solution using LinkedList

class LRUCache:
    class MyNode:
        def __init__(self, key: int = -1, value: int = -1):
            self.key: int = key
            self.value: int = value
            self.prev: LRUCache.MyNode = None
            self.next: LRUCache.MyNode = None

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.data: dict[int, LRUCache.MyNode] = {}
        self.head: LRUCache.MyNode = LRUCache.MyNode()
        self.tail: LRUCache.MyNode = LRUCache.MyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node: MyNode) -> None:
        after_head = self.head.next
        node.next = after_head
        node.prev = self.head
        after_head.prev = node
        self.head.next = node

    def del_node(self, node: MyNode) -> None:
        before_node = node.prev
        after_node = node.next
        before_node.next = after_node
        after_node.prev = before_node

    def move_node(self, node: MyNode) -> None:
        self.del_node(node)
        self.add_node(node)

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        node = self.data.pop(key)
        self.move_node(node)
        self.data[key] = self.head.next
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            node.value = value
            self.move_node(node)
            self.data[key] = self.head.next
        else:
            if len(self.data) == self.capacity:
                node = self.tail.prev
                del self.data[node.key]
                self.del_node(node)
            new_node = LRUCache.MyNode(key, value)
            self.add_node(new_node)
            self.data[key] = self.head.next
