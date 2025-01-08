class Trie:

    class Node:  
        def __init__(self):
            self.hashmap = {}
            self.isWord = False


    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char in curr.hashmap:
                curr = curr.hashmap[char]
            else:
                newNode = self.Node()
                curr.hashmap[char] = newNode
                curr = newNode
        
        curr.isWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.hashmap:
                return False
            else:
                curr = curr.hashmap[char]

        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.hashmap:
                return False
            else:
                curr = curr.hashmap[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)