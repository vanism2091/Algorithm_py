import itertools
from typing import *
# https://leetcode.com/problems/permutations/

"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # sol_2-book: itertools 모듈 사용
        return list(itertools.permutations(nums))

        # sol_2-b_mine: 
        # 아래 코드의 출력은 각 elem이 tuple인데, 릿코드에선 정답 판정
        return list(itertools.permutations(nums))
        # return list(map(list, itertools.permutations(nums)))
        
        # sol_1-book: DFS를 이용한 순열 생성
        results = []
        prev_elements = []
        
        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                ### [:]로 copy하지 않으면 참조가 됨. 이후에 prev 값 변경 시 results의 원소가 영향 받음
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        dfs(nums)
        return results

        # mine: 일단 brute-force로
        res: List[List[int]] = []
        def btr(nums:List[int], curr:List[int]=[]):
            if not nums:
                res.append(curr)
                return
            for i in nums:
                btr([n for n in nums if n != i], [*curr, i])
        btr(nums)
        return res