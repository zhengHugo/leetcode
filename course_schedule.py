from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = [False] * numCourses
        self.checked = [False] * numCourses
        self.neighbors = [[] for i in range(numCourses)]
        for edge in prerequisites:
            self.neighbors[edge[0]].append(edge[1])

        def helper(v: int) -> bool:
            self.visited[v] = True
            if not self.neighbors[v] or self.checked[v]:
                self.checked[v] = True
                return True

            for u in self.neighbors[v]:
                if self.checked[u]:
                    continue
                elif self.visited[u] or not helper(u):
                    return False
                
            self.checked[v] = True
            return True

        for v in range(numCourses):
            self.visited = [False] * numCourses
            if not self.checked[v]:
                if not helper(v):
                    return False
        return True


s = Solution()
print(s.canFinish(3, [[0, 1], [0, 2], [1, 2]]))
