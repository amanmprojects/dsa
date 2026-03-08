from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = 0
        for n in nums:
            curr = curr ^ n
        return curr