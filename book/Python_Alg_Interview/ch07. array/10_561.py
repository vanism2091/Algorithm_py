from typing import *
# https://leetcode.com/problems/array-partition/


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ## 261ms
        nums.sort()
        total = 0
        for i in range(len(nums) // 2):
            total += nums[2*i]
        return total
        ## 빠른 풀이 2
        nums.sort()
        shot=0
        for i in range(0,len(nums),2):
            shot+=nums[i]
        return shot

        # sol_3-book pythonic
        # 내 첫 풀이와 같음
        
        # sol_2-book even
        sum = 0
        nums.sort()
        
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum

        # sol_1-book ascending
        sum = 0
        pair = []
        nums.sort()
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += pair[0]
                pair = []
        
        return sum

        # mine
        # O(nlogn)
        return sum(sorted(nums)[::2])