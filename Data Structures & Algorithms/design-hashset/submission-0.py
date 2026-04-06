class MyHashSet:

    def __init__(self):
        self.size = 100003
        self.buckets = [[] for _ in range(self.size)]
        

    def add(self, key: int) -> None:
        if key in self.buckets[key % self.size]:
            return
        
        self.buckets[key % self.size].append(key)

    def remove(self, key: int) -> None:
        if key in self.buckets[key % self.size]:
            self.buckets[key % self.size].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[key % self.size]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)