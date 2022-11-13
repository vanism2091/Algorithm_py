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
        # mine
        tickets.sort()
        dict = collections.defaultdict(Deque)
        for [dep, arr] in tickets:
            dict[dep].append(arr)
        
        self.path = ["JFK"]
        def dfs(departure: str, curr:list = []):
            if len(curr) == len(tickets):
                curr.append(dict[departure].popleft())
                self.path = curr[:]
                return True
            while dict[departure]:
                arrival = dict[departure].popleft()
                r_idx = 0
                while arrival not in dict and dict[departure]:
                    r_idx += 1
                    dict[departure].append(arrival)
                    arrival = dict[departure].popleft()
                if r_idx > 0:
                    dict[departure].rotate(r_idx)
                if dfs(arrival, curr + [arrival]):
                    break
            return False
                    
        dfs("JFK", self.path)
        return self.path

tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
s = Solution()
a = s.findItinerary(tickets)

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