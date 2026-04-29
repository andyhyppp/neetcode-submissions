class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True


    def search(self, word: str) -> bool:
        
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return False
        return cur.is_end


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return False
        return True
        