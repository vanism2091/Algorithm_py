import collections
from typing import *
# https://leetcode.com/problems/reconstruct-itinerary/

"""
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints
- 1 <= tickets.length <= 300
- tickets[i].length == 2
- from_i.length == 3
- to_i.length == 3
- from_i and to_i consist of uppercase English letters.
- from_i != to_i
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sol_3-book: 일정 그래프 반복
            # 재귀 구조 대신 반복으로
            # 3-b_mine이랑 큰 논리는 같은데, 코드 되게 깔끔... :)
        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]


        # sol_3-b_mine: 일정 그래프 반복
        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route = []
        stack = ['JFK']
        while stack:
            curr = stack[-1]
            
            if graph[curr]:
                stack.append(graph[curr].pop())
            else: 
                route.append(stack.pop())
            
        return route[::-1]
                
        def dfs(a):
            # 마지막 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]


        # sol_2-book: 스택 연산으로 큐 연산 최적화 시도
            # pop(0): O(N) 
            # pop(): O(1)
            # 리트코드에서는 N이 작아 유의미한 차이가 없었지만, 데이터가 크면 그렇지 않음
        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            # 마지막 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

        # sol_1-book: DFS로 일정 그래프 구성
            # 1. 그래프 구성
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
s = Solution()
a = s.findItinerary(tickets)
print(a)

# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         # mine
#         # 1. sort
#         # 2. dfs로 확인 후, 다 되는지 체크, 그리고 안된다면 ㄴㄴ

#         tickets.sort()
#         dict = collections.defaultdict(Deque)
#         for [dep, arr] in tickets:
#             dict[dep].append(arr)
        
#         path = []
#         self.done = False
#         def dfs(depart: str, curr:list = []):
#             if self.done:
#                 return
#             if len(curr) == len(tickets):
#                 global path
#                 path = curr[:]
#                 self.done = True
#                 return
#             for arrival in dict[depart]:
#                 dfs(arrival, curr + [depart])
#         return path