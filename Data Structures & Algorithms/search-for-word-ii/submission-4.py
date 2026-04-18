class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store full word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word


class Solution:
    def findWords(self, board, words):
        ROWS, COLS = len(board), len(board[0])

        trie = Trie()
        for w in words:
            trie.insert(w)

        res = []

        def dfs(r, c, node):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] not in node.children
            ):
                return

            char = board[r][c]
            node = node.children[char]

            if node.word:
                res.append(node.word)
                node.word = None  # avoid duplicates

            board[r][c] = "#"  # mark visited

            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)

            board[r][c] = char  # restore

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root)

        return res