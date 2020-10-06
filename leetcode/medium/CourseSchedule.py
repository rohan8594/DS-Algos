# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish
# all courses?

# Example 1:
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.

# Logic:
# if node v has not been visited, then mark it as 0.
# if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
# if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its
# successors.

import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: 'List[List[int]]') -> bool:
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(int)

        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(v):
            if visited[v] == -1:
                return False
            if visited[v] == 1:
                return True
            visited[v] = -1
            for u in graph[v]:
                if not dfs(u):
                    return False
            visited[v] = 1
            return True

        for v in range(numCourses):
            if not dfs(v):
                return False
        return True
