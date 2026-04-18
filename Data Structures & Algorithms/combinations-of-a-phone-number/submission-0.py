from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        s = ""

        def dfs(i):
            nonlocal s
            if i >= len(digits):
                res.append(s)
                return
            
            for val in keypad[digits[i]]:
                s += val
                dfs(i + 1)
                s = s[:-1]

        dfs(0)

        return res
