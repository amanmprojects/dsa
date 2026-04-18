from typing import Optional

class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev, self.next = None, None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # This are boundary pointers and will not hold actual values
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def insertAtRight(self, n: Node):
        # Adds node n to the rightmost end of DLL
        prev = self.right.prev

        # Link between prev and n
        prev.next = n
        n.prev = prev

        # Link between n and right
        n.next = self.right
        self.right.prev = n

    def remove(self, n: Node):
        # Remove node n from the double Linked list
        prev = n.prev
        prev.next = n.next
        n.next.prev = prev
        n.next, n.prev = None, None

    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache[key].val
            self.remove(self.cache[key])
            self.insertAtRight(self.cache[key])
            return res

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key already in cache, update value and move to right
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insertAtRight(self.cache[key])
        else:
            # If key not in cache, create new node, add it to cache as key=Node, and insert the node to right of LL
            n = Node(key, val=value)
            self.cache[key] = n
            self.insertAtRight(n)

        # If cache overflow, then remove least recently used (leftmost value)
        if len(self.cache) > self.capacity:
            if not (len(self.cache) == 0):
                n = self.left.next
                self.remove(n)
                del self.cache[n.key]


        
