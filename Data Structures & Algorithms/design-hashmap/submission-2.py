class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size
        
    def put(self, key: int, value: int) -> None:
        bi = self.hash(key)
        bucket = self.buckets[bi]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                bucket.append((key, value))
                return 
            
        bucket.append((key, value))

    def get(self, key: int) -> int:
        bi = self.hash(key)
        bucket = self.buckets[bi]

        for (k, v) in bucket:
            if k == key:
                return v
        
        return -1
        

    def remove(self, key: int) -> None:
        bi = self.hash(key)
        bucket = self.buckets[bi]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return 
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


    # def __init__(self):
    #     self.size = 1000
    #     self.buckets = [[] for _ in range(self.size)]
        

    # def add(self, key: int) -> None:
    #     if key in self.buckets[key % self.size]:
    #         return
        
    #     self.buckets[key % self.size].append(key)

    # def remove(self, key: int) -> None:
    #     if key in self.buckets[key % self.size]:
    #         self.buckets[key % self.size].remove(key)

    # def contains(self, key: int) -> bool:
    #     return key in self.buckets[key % self.size]