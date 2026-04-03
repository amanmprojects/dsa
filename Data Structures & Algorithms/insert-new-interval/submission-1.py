class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervalsCopy = intervals.copy()

        i = 0
        while i < len(intervalsCopy) and intervalsCopy[i][0] < newInterval[0]:
            i += 1
            
        intervalsCopy.insert(i, newInterval)

        # Optional but safer
        intervalsCopy.sort()

        j = 0
        while j < len(intervalsCopy) - 1:
            if intervalsCopy[j][1] >= intervalsCopy[j+1][0]:
                mergedInterval = [
                    min(intervalsCopy[j][0], intervalsCopy[j+1][0]),
                    max(intervalsCopy[j][1], intervalsCopy[j+1][1])
                ]
                intervalsCopy.pop(j)
                intervalsCopy.pop(j)
                intervalsCopy.insert(j, mergedInterval)
            else:
                j += 1

        return intervalsCopy