import itertools
from typing import *
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 이번 문제는 배울게 많음

        # sol_1-book: 트리의 모든 DFS 결과
        # 탐색 하는 과정 자체가 하나의 결과임
        results = []

        def dfs(index, path):
            # 매번 결과 추가
            results.append(path)
            
            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0, [])
        return results
        
        # mine2 itertools 사용
        # list comprehension 안에서 *를 쓸 수 없음. for in for in 2번 써서 해결
        # https://stackoverflow.com/questions/13958998/python-list-comprehension-unpacking-and-multiple-operations
        return [tup for i in range(len(nums)+1) for tup in itertools.combinations(nums, i)]
        # return [list(itertools.combinations(nums, i)) for i in range(len(nums)+1)]
        
        # mine
        # 음.. 이전에 풀었던 조합문제에서 k를 1부터 len(nums)까지..
        res = [[]]
        def dfs(nums: List[int], cnt:int, curr=[]):
            if cnt == 0:
                res.append(curr)
                return
            for i, num in enumerate(nums):
                dfs(nums[i+1:], cnt-1, curr + [num])
        for i in range(1, len(nums)+1):
            dfs(nums, i)
        return res