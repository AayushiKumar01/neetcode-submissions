class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        results = []

        for start, end in intervals:
            if not results or start > results[-1][1]:
                results.append([start,end])

            else:
                results[-1][1] = max(results[-1][1],end)
        
        return results
        