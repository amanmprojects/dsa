import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max heap by pushing negatives
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, -(first - second))

        return -stones[0] if stones else 0