class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append([v,w])

        dist = [float("inf")] * (n+1)
        dist[k] = 0

        heap = [(0,k)]

        while heap:
            time,node = heapq.heappop(heap)

            for neighbor, weight in graph[node]:
                new_time = time + weight
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap,(new_time,neighbor))
        max_time = max(dist[1:])

        if max_time == float("inf"):
            return -1
        
        return max_time

            