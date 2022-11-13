from typing import *
# https://leetcode.com/problems/combination-sum/


"""
Example 1:
* Input: candidates = [2,3,6,7], target = 7
* Output: [[2,2,3],[7]]
* Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

Example 2:
* Input: candidates = [2,3,5], target = 8
* Output: [[2,2,2,2],[2,3,3],[3,5]]

Constraints
* 1 <= candidates.length <= 30
* 2 <= candidates[i] <= 40
* All elements of candidates are distinct.
* 1 <= target <= 500
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # sol_1-book: DFS로 중복 조합 그래프 탐색
        results = []
        
        def dfs(csum, index, path):
            # 종료 조건
            if csum == 0:
                results.append(path)
                return
            if csum < 0:
                return
            
            # 자신부터 하위 원소 까지의 나열 재귀 호출            
            for i in range(index, len(candidates)):
                ### 조합
                dfs(csum - candidates[i], i, path + [candidates[i]])
                ### 순열
                # dfs(csum - candidates[i], 0, path + [candidates])
        
        dfs(target, 0, [])
        return results

        # mine
        # 백트래킹
        res = []
        def btr(cands: List[int], target, curr:List[int]=[]):
            if target == 0:
                res.append(curr)
                return
            if target < 0 or not cands:
                return
            
            for i, num in enumerate(cands):
                btr(cands[i:], target - num, [*curr, num])
        btr(candidates, target)
        return res
                