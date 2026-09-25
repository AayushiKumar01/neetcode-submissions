class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals)-1
        while l <= r:
            mid = (l+r) // 2
            if intervals[mid][0] < newInterval[0]:
                l = l+ 1
            else:
                r = r - 1
        
        intervals.insert(l,newInterval)

        result = []

        for start, end in intervals:

            if not result or start > result[-1][1]:
                result.append([start, end])

            else:
                result[-1][1] = max(result[-1][1], end)

        return result
        