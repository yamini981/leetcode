# I'm thinking a trie...
# So like a tree where each layer has 26 potential continues
# Each node has a hashmap with key: character value: NextNode

class WordDictionary:

    class Node:

        def __init__(self, depth):
            self.depth = depth
            self.isWord = False
            self.hashmap = {}



    def __init__(self):
        self.root = self.Node(0)

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.hashmap:
                curr.hashmap[char] = self.Node(curr.depth + 1)
            curr = curr.hashmap[char]

        curr.isWord = True

    def search(self, word: str) -> bool:
        # Perhaps use a queue for 'curr' node?

        # added root 0 b 1 a 2 d 3
        # searching . a d
        q = collections.deque()
        q.append(self.root)
        while q:
            curr = q.pop()
            if len(word) == curr.depth:
                if curr.isWord:
                    return True
                else:
                    continue

            char = word[curr.depth]
            if char == '.':
                for key in curr.hashmap:
                    q.append(curr.hashmap[key])
            else:
                if char in curr.hashmap:
                    q.append(curr.hashmap[char])

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)