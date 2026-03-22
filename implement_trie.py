from typing import Optional


class TrieNode:
    def __init__(self, val: Optional[str], isComplete: bool = False):
        self.val = val
        self.children = dict[str, TrieNode]()
        self.isComplete = isComplete


class PrefixTree:
    def __init__(self):
        self.root = TrieNode(val=None)

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode(val=char)
                curr = curr.children[char]

        curr.isComplete = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.isComplete

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
