from typing import List
from math import log2, floor

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            if i < 4:
                curr = i
                count = 0
                while curr != 0:
                    if(curr%2==1): count += 1
                    curr = curr>>1
                res.append(count)
                continue
            
            offset = 2**floor(log2(i))
            res[i] = 1 + res[i-offset]
            
