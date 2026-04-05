class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            res.append(int.bit_count(i))
        
        return res