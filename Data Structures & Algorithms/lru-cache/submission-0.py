
class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node_map = {}
        self.right = Node(0, 0)
        self.left = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev
        
    def insert(self, node):
        # insert before the right
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev
        

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1

        # get the value
        self.remove(self.key_node_map[key])
        self.insert(self.key_node_map[key])
        
        return self.key_node_map[key].val

    def put(self, key: int, value: int) -> None:
        
        if key in self.key_node_map:
            node = self.key_node_map[key]
            self.remove(node)

        node = Node(key, value)
        self.key_node_map[key] = node
        self.insert(node)

        if len(self.key_node_map) > self.capacity:
            # remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.key_node_map[lru.key]


        








