from typing import Optional


class TrieNode:
    def __init__(self, val: Optional[str], isComplete: bool = False):
        self.val = val
        self.children = dict[str, TrieNode]()
        self.isComplete = isComplete


class WordDictionary:
    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode(val=char)
                curr = curr.children[char]

        curr.isComplete = True

    def search(self, word: str, curr=None) -> bool:
        if curr is None:
            curr = self.root

        for i in range(len(word)):
            if word[i] == ".":
                for child in curr.children:
                    if self.search(word[i + 1 :], curr=curr.children[child]):
                        return True
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                return False

        return curr.isComplete
