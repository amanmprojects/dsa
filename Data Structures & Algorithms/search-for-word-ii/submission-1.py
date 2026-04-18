from typing import List


class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = dict[str, TrieNode]()
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(val=char)
            curr = curr.children[char]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        # Insert all words in the word trie
        word_trie = Trie()
        for word in words:
            word_trie.insert(word=word)

        res = set()
        path = set()
        s = ""
        curr = word_trie.root

        def dfs(r, c):
            nonlocal s, curr
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or board[r][c] not in curr.children
                or (r, c) in path
            ):
                return

            s += board[r][c]
            temp_curr = curr
            curr = curr.children[board[r][c]]
            path.add((r, c))

            if curr.isWord:
                res.add(s)

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            s = s[:-1]
            curr = temp_curr
            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)

        return list(res)
