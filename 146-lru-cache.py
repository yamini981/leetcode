class ListNode:
    def __init__(self, val=0, nextNode=None, prevNode =None, key=0):
        self.val = val
        self.next = nextNode
        self.prev = prevNode
        self.key = key


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.tail = None
        self.head = None
        # can use LinkedList nodes as items in dictionary
        # if you're getting/putting a key, you should move your current node
        # to the top of the linked list (newHead)
        # if you're at capacity, remove the tail of the linked list
        
    def removeNodeFromList(self, node):
        prevNode = node.prev
        nextNode = node.next
        if node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.next = None
        if prevNode and nextNode:
            nextNode.prev = prevNode
            prevNode.next = nextNode
            node.next = None
            node.prev = None
        elif prevNode:
            prevNode.next = None
            node.prev = None
        # probably never happens, since we're usually going to 
        # just put stuff at the head, but still going to implement
        elif nextNode:
            nextNode.prev = None
            node.next = None
        else:
            node.next = None
            node.prev = None


    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        # must do this every time
        currNode = self.dict[key]
        retVal = currNode.val
        # remove node from the linked list and put it at the top 
        # meaning it's the most recently used

        # don't need to do anything if it's already at the head
        if self.head != currNode:
            self.removeNodeFromList(currNode)
            self.head.prev = currNode
            currNode.next = self.head
            self.head = currNode
            if self.capacity == 1:
                self.tail = currNode

        return retVal
            
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            # need to update the value
            currNode = self.dict[key]
            currNode.val = value
        else:
            # need to add in the value
            currNode = ListNode(value, None, None, key)
            self.dict[key] = currNode
            if self.head == None:
                self.head = currNode
                self.tail = currNode
            else:
                
                # need to remove least recently used (tail) IF we at capacity
                if len(self.dict) > self.capacity:
                    
                    # tail should be updated in removeNodeFromList
                    del self.dict[self.tail.key]
                    self.removeNodeFromList(self.tail)

        # need to mark as most recently used
        if self.head != currNode:
            self.removeNodeFromList(currNode)
            if self.head:
                self.head.prev = currNode
                currNode.next = self.head
            self.head = currNode
            if self.capacity == 1:
                self.tail = currNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)