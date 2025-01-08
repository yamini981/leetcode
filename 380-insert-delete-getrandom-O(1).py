import random

class RandomizedSet:

    def __init__(self):
        self.randomSet = {}
        self.randomList = []

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        self.randomSet[val] = len(self.randomList)
        self.randomList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False

        currIndex = self.randomSet[val]
        self.randomSet.pop(val)
        lastElement = self.randomList.pop()
        if currIndex != len(self.randomList):
            self.randomList[currIndex] = lastElement
            self.randomSet[lastElement] = currIndex
        return True

    def getRandom(self) -> int:
        return random.choice(self.randomList)
        # can't store values in random places because then you can't remove/insert in O(1)
        # [ 1 3 7 ]
        # best way would be to use some algorithm to choose a random value... 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()