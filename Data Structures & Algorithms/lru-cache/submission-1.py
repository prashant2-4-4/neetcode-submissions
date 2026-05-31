class Node:
    def __init__(self , key , val , next =None , prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}

        # dummy nodes
        self.left = Node(0, 0)   # LRU end
        self.right = Node(0, 0)  # MRU end
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def remove_lru(self):
        lru_node = self.left.next
        self.left.next = lru_node.next
        lru_node.next.prev = self.left
        del self.hash_map[lru_node.key]

    def insert_mru(self, node):
        # always insert before dummy right
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key in self.hash_map:
            node = self.hash_map[key]
            self.remove(node)
            self.insert_mru(node)  # move to MRU, update hash_map not needed since same node
            return node.val
        return -1

    def put(self ,key , value):
        if key in self.hash_map:
            node = self.hash_map[key]
            self.hash_map[key].val = value
            self.remove(node)
            self.insert_mru(node)
        else:
            node = Node(key ,value)
            if len(self.hash_map) + 1 <= self.capacity:
                self.insert_mru(node)
            else:
                self.remove_lru() 
                self.insert_mru(node)
            self.hash_map[key] = node
        