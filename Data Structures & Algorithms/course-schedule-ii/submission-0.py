class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1 

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
            course = q.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)


        if len(order) == numCourses:
            return order
        return []


        
        