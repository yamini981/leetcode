class Solution:

    class Trie:
        class Node:
            def __init__(self):
                self.hashmap = {}
                self.isWord = False
        
        def __init__(self):
            self.root = self.Node()

        def insert(self, word):
            curr = self.root

            for char in word:
                if char not in curr.hashmap:
                    curr.hashmap[char] = self.Node()
                
                curr = curr.hashmap[char]
            curr.isWord = True
            curr.word = word
        
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # thinking - create a Trie for all of the words in the dictionary
        # then check each square and see if it can recreate any words in the Trie...
        mainTrie = self.Trie()
        for word in words:
            mainTrie.insert(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(i, j, trieNode, word):
            if (i < 0 or j < 0 or
                i == ROWS or j == COLS or
                (i, j) in visit or board[i][j] not in trieNode.hashmap):
                return 
            
            visit.add((i, j))

            trieNode = trieNode.hashmap[board[i][j]]
            word += board[i][j]
            if trieNode.isWord:
                res.add(word)

            dfs(i + 1, j, trieNode, word)
            dfs(i - 1, j, trieNode, word)
            dfs(i, j + 1, trieNode, word)
            dfs(i, j - 1, trieNode, word)

            visit.remove((i, j))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, mainTrie.root, "")

        return list(res)