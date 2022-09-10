"""
https://leetcode.com/problems/two-sum/

1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sol_4 one loop
        nums_map = {}
        for i, num in enumerate(nums):
            t = target - num
            if t in nums_map:
                return nums_map[t], i
            nums_map[num] = i
        
        # sol_3 key
        num_dict = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            t = target - num
            if t in num_dict and num_dict[t] != i:
                return [i, num_dict[t]]

        
        # sol_2 in operation
        for i, num in enumerate(nums):
            t = target - num
            if t in nums[i+1:]:
                return i, nums[i+1:].index(t) + i + 1
        
        # sol_1 brute force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
             
    
    
    
    
    """
    Mine 2: use bisect
    
    from bisect import bisect_left
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted([(i, num) for i, num in enumerate(nums)], key=lambda x: x[1])
        def index(a: list, x: int) -> int:
            i = bisect_left(a, x, key=lambda x: x[1])
            if i != len(a) and a[i][1] == x:
                return i
            return -1
            
        for i, (idx, num) in enumerate(sorted_nums):
            j = index(sorted_nums, target-num)
            if j != i and j != -1:
                return [idx, sorted_nums[j][0]]        
    """  
        
    """
        # brute force
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    """