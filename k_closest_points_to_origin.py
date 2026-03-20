import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        distances = [(sqrt(point[0] ** 2 + point[1] ** 2), point) for point in points]

        heapq.heapify(distances)

        for i in range(k):
            dist, point = heapq.heappop(distances)
            res.append(point)

        return res