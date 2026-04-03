class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        res = []
        curr = intervals[0]
        for interval in intervals:
            if curr[0] > interval[1]:
                res.append(interval)
            elif curr[1] < interval[0]:
                res.append(curr)
                curr = interval
            else:
                curr[0] = min(curr[0], interval[0])
                curr[1] = max(curr[1], interval[1])
        
        res.append(curr)

        return res
