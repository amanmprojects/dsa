from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)

        print(graph)
        
        
        path = set()
        visited = set()




        stack = []

        def dfs(x):
            if x in path:
                print("In path")
                return False
                
            if x in visited:
                return True
            

            path.add(x)
            for child in graph[x]:
                if not dfs(child):
                    print(f"child: {child} failed babes")
                    return False
            path.remove(x)
            
            visited.add(x)
            stack.append(x)

            return True
        
        for course in graph:
            if not dfs(course):
                print(f"not dfs of {course}")
                return []
            
        return stack[::-1]

