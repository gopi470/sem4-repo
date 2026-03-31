from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()

        # Push nodes with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        # BFS
        while q:
            u = q.popleft()
            count += 1

            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return count == numCourses