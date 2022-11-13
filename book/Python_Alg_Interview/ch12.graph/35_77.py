import itertools
from typing import *
# https://leetcode.com/problems/combinations/

"""
Input: 
    n = 4, k = 2
Output: 
    [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: 
    There are 4 choose 2 = 6 total combinations.
    Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Constraints:
* 1 <= n <= 20
* 1 <= k <= n
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # sol_2-b-mine: itertools 사용
        # Runtime: 163 ms, faster than 83.40% of Python3 online submissions for Combinations.
        return list(itertools.combinations(range(1,n+1), k))
        
        # sol_1-book: DFS로 k개 조합 생성
        results = []
        def dfs(elements:List[int], start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            
            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        
        dfs([], 1, k)
        return results


        # 일단 brute-force로
        # 엄청 오래 걸림.. :) 
        # 1196 ms, faster than 7.15% of Python3 online submissions for Combinations.
        res: List[List[int]] = []
        def btr(nums:List[int], cnt:int, curr:List[int]=[]):
            if cnt == 0:
                res.append(curr)
                return
            for i, num in enumerate(nums):
                btr(nums[i+1:], cnt-1, [*curr, num] )
        btr(list(range(1, n+1)), k)
        return res