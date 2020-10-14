class Node:
    def __init__(self, value=False, key=False):
        self.value = value
        self.key = key
        self.next = False
        self.prev = False


class DLL:
    def __init__(self, n):
        self.max_size = n
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.current = self.head

    def remove(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.size -= 1

    def unshift(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1


class LRUCache:
    def __init__(self, capacity: int):

        self.dll = DLL(capacity)
        self.hashmap = {}

    def get(self, key: int) -> int:

        if key in self.hashmap.keys():
            self.dll.remove(self.hashmap[key])
            self.dll.unshift(self.hashmap[key])
            return self.hashmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap.keys():
            node = self.hashmap[key]
            self.dll.remove(node)
            self.dll.unshift(node)
        else:
            node = Node(value, key)
            if self.dll.size == self.dll.max_size:
                self.hashmap.pop(self.dll.tail.prev.key)
                self.dll.remove(self.dll.tail)
                self.dll.unshift(node)
                self.hashmap[key] = node
            else:
                self.hashmap[key] = node
                self.dll.unshift(node)


# orders = ["LRUCache", "put", "get", "put", "get", "get"]
# values = [[1], [2, 1], [2], [3, 2], [2], [3]]

orders = [
    "LRUCache",
    "put",
    "put",
    "put",
    "put",
    "get",
    "get",
    "get",
    "get",
    "put",
    "get",
    "get",
    "get",
    "get",
    "get",
]
values = [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]]

for idx, order in enumerate(orders):
    if idx == 0:
        LRU = LRUCache(values[0][0])
    if order == "put":
        LRU.put(values[idx][0], values[idx][1])
    if order == "get":
        LRU.get(values[idx][0])