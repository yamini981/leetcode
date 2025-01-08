class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # {letter: word}
        # {word}

        hashmap = {}
        wordSet = set()

        wordList = s.split(' ')

        if len(wordList) != len(pattern):
            return False

        for i in range(len(pattern)):
            currChar = pattern[i]
            currWord = wordList[i]

            if currChar not in hashmap:
                if currWord in wordSet:
                    return False
                hashmap[currChar] = currWord
                wordSet.add(currWord)
            else:
                if currWord != hashmap[currChar]:
                    return False

        return True
                