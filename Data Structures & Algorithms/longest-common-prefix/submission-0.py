class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs[0]:
            return res
        
        for i in range(len(strs[0])):
            print(strs[0][i])
            for s in strs:
                if i >= len(s):
                    return res
                
                if s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res
                

