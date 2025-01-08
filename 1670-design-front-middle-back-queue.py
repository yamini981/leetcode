class Node:
        def __init__(self, value):
            self.next = None
            self.prev = None
            self.val = value

class FrontMiddleBackQueue:
    

    
    def __init__(self):
        self.head = None
        self.tail = None
        self.mid = None
        self.length = 0

    def pushFront(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.mid = newNode
            self.length += 1
            return
            
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

        self.length += 1

        if self.length % 2 == 0:
            self.mid = self.mid.prev


    def pushMiddle(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.mid = newNode
            self.length += 1
            return

        self.length += 1

        if self.length == 2:
            self.mid = newNode
            self.head = newNode
            self.tail.prev = newNode
            newNode.next = self.tail
        elif self.length == 3:
            self.mid = newNode
            newNode.next = self.tail
            newNode.prev = self.head
            self.head.next = newNode
            self.tail.prev = newNode
        elif self.length % 2 == 0:
            newNode.next = self.mid
            newNode.prev = self.mid.prev
            self.mid.prev.next = newNode
            self.mid.prev = newNode
            self.mid = newNode
        else:
            newNode.next = self.mid.next
            newNode.prev = self.mid
            self.mid.next.prev = newNode
            self.mid.next = newNode
            self.mid = newNode
        

    def pushBack(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.mid = newNode
            self.length += 1
            return

        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

        self.length += 1

        if self.length %2 == 1:
            self.mid = self.mid.next

    def popFront(self) -> int:
        if self.length == 0:
            return -1
        retVal = self.head.val
        if self.length == 1:
            self.length -= 1
            self.head = None
            self.tail = None
            self.mid = None
            return retVal

        self.head = self.head.next
        self.head.prev = None

        

        self.length -= 1

        if self.length % 2 == 1:
            self.mid = self.mid.next

        
        return retVal


    def popMiddle(self) -> int:
        if self.length == 0:
            return -1
        retVal = self.mid.val
        if self.length == 1:
            self.length -= 1
            self.head = None
            self.tail = None
            self.mid = None
            return retVal
        if self.length == 2:
            self.length -= 1
            self.mid = self.tail
            self.head = self.tail
            self.mid.prev = None
            return retVal

        tempPrev = self.mid.prev
        tempNext = self.mid.next
        tempPrev.next = tempNext
        tempNext.prev = tempPrev

        self.length -= 1

        if self.length % 2 == 1:
            self.mid = tempNext
        else:
            self.mid = tempPrev

        return retVal
    def popBack(self) -> int:
        if self.length == 0:
            return -1
        retVal = self.tail.val
        if self.length == 1:
            self.length -= 1
            self.head = None
            self.tail = None
            self.mid = None
            return retVal
        
        self.tail = self.tail.prev
        self.tail.next = None

        self.length -= 1

        if self.length % 2 == 0:
            self.mid = self.mid.prev
        return retVal

        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()