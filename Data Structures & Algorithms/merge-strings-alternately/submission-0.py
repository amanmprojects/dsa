class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ''
        total = len(word1) + len(word2)

        while (i + j) < total:
            if i < len(word1):
                res += word1[i]
                i += 1

            if j < len(word2):
                res += word2[j]
                j += 1
            
        return res

