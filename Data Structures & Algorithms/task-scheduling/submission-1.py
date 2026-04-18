import heapq
from collections import deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = {task: 0 for task in tasks}
        for task in tasks:
            freq_dict[task] += 1

        freq_list = [(-freq_dict[t], t) for t in freq_dict]

        heapq.heapify(freq_list)

        time = 0

        queue = deque([])

        while freq_list or queue:
            if freq_list:
                neg_freq, task = heapq.heappop(freq_list)
                neg_freq += 1
                if neg_freq < 0:
                    nextT = time + n
                    queue.append((nextT, neg_freq, task))

            if queue:
                while queue and queue[0][0] <= time:
                    curr = queue.popleft()
                    heapq.heappush(freq_list, (curr[1], curr[2]))

            time += 1

        return time
