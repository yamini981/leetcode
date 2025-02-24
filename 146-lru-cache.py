class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # stack with []
        self.elementCount = 0
        # dict with key : (value, keyNode)
        # needs to be some kind of stack I think...
        # if something is recently used it's added to the front of the stack
        # 
        self.dict = OrderedDict()

        

    def get(self, key: int) -> int:
        # need to move keyQueue around
        
        if key not in self.dict:
            return -1

        self.dict.move_to_end(key)
        return self.dict[key]
    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            self.elementCount += 1

        self.dict[key] = value
        self.dict.move_to_end(key)

        if self.elementCount > self.capacity:
            self.dict.popitem(False)
            self.elementCount -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)