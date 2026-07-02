from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exacts = set()
        caseins = {}
        vowins = {}

        def f(s):
            res = []

            for c in s:
                if c in "aeiou":
                    res.append("*")
                else:
                    res.append(c)

            return "".join(res)

        for word in wordlist:
            exacts.add(word)
            lower = word.lower()
            caseins.setdefault(lower, word)
            vowins.setdefault(f(lower), word)

        result = []


        for query in queries:
            query_lower = query.lower()
            query_vowels = f(query_lower)
            
            if query in exacts:
                result.append(query)
                print("exacts")
                
            elif query_lower in caseins:
                result.append(caseins[query_lower])
                print("caseins")
                
            elif query_vowels in vowins:
                result.append(vowins[query_vowels])
                print("vowins")
            
            else:
                result.append("")
            
        return result

sol = Solution()