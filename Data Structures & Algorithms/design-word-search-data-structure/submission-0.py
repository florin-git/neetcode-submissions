class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.trie

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.trie

        return self._search(word, cur)

    def _search(self, word: str, cur: TrieNode) -> bool:

        for i, c in enumerate(word):
            if c == ".":
                for ch in cur.children.values():
                    if self._search(word[i + 1:], ch):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                cur = cur.children[c]

        return cur.is_end 




        
