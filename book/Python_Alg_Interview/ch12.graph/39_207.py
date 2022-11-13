import collections
from typing import *
# https://leetcode.com/problems/course-schedule/

"""

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # sol_2-book: 가지치기를 이용한 최적화
        # 한 번 방문했던 그래프는 두 번 방문하지 않도록 무조건 True로 리턴한다.
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced, visited = set(), set()
        
        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문했던 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            return True
        
        # 순환 구조 판별
        for k in list(graph):
            if not dfs(k):
                return False
        return True

        
        # sol_1-book : DFS로 순환 구조 판별
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                    return False
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True

        # sol_1-b_mine : DFS로 순환 구조 판별
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()

        def dfs(c):
            while graph[c]:
                if graph[c][-1] in traced:
                    return False
                traced.add(graph[c][-1])
                return dfs(graph[c].pop())
            return True

        for x in graph:
            if not dfs(x):
                return False
        return True
        
        # mine
        # 6.40 / 5.25
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        cycle = []
        def dfs(c, arr=[]):
            while graph[c]:
                dfs(graph[c].pop(), arr+[c])
            
            if c in arr:
                cycle.append(c)            
            
        for k in list(graph.keys()):
            dfs(k)
            if len(cycle) > 0:
                return False
        return True
    

        # mine - 불가능
        graph = collections.defaultdict(list)
        for a, b in numCourses:
            graph[a].append(b)
        res = True
        def dfs(c, arr=[]):
            if c in arr:
                return False
            while graph[c]:
                n = graph[c].pop()
                dfs(n, arr + [n])
            return True
        
        for k in graph:
            res = res and dfs(k)
        return res