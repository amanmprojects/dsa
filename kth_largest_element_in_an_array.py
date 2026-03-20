import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0

        neg_nums = [-n for n in nums]

        heapq.heapify(neg_nums)

        for i in range(k):
            res = -heapq.heappop(neg_nums)

        return res
