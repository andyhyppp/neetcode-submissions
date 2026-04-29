class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self,word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end= True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root= TrieNode()

        for word in words:
            root.addWord(word)
        
        m, n = len(board), len(board[0])
        visited = set()
        res = set()

        def dfs(r,c, node, word):
            if (0>r or r>=m or 0>c or c>=n or (r,c) in visited or board[r][c] not in node.children):
                return
            visited.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.is_end:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))
        
        for r in range(m):
            for c in range(n):
                dfs(r,c,root,"")
        return list(res)