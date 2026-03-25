from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list
        preMap = {}

        for p in prerequisites:
            if p[0] not in preMap:
                preMap[p[0]] = set()
            preMap[p[0]].add(p[1])

        path = set()

        def dfs(course):
            if course in path:
                return False

            if course not in preMap:
                return True

            if not preMap[course]:
                preMap.pop(course)
                return True

            path.add(course)
            for p in preMap[course]:
                if dfs(p):
                    preMap[course].remove(p)
            path.remove(course)

        for course in preMap:
            if not dfs(course):
                return False

        return True
