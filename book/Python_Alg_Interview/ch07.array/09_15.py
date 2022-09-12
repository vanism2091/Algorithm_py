from typing import *
# https://leetcode.com/problems/3sum/
"""
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, 
        and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # two pointer - book
        """
        - if elif else 에 걸쳐서 계속 합을 이용한다면, sum이라는 변수에서 한다.
        - 스킵 처리는 정답일 때에만 한다.
        """
        results = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # 0일 때, 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
        return results

        # two pointer로 합계산  - mine
        results = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                if (left > i+1 and nums[left] == nums[left-1]):
                    left += 1
                    continue
                if (right < len(nums)-2 and nums[right] == nums[right+1]):
                    right -= 1
                    continue
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
        return results

        # brute-force-book O(n**3)
        results = []
        nums.sort()
        for i in range(len(nums)-2):
            # 중복값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])
        return results
        
        # brute-force-mine
        res = set()
        nums.sort()
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if num + nums[j] + nums[k] == 0:
                        res.add((num, nums[j], nums[k]))
        return [list(tup) for tup in res]
        
        
        
        
        # mine
        # time limite Exceeded.. :(
        res = set()
        def twoSum(nums: List[int], target: int, res: List[List[int]]) -> List[int]:
            nums_map = {}
            for i, num in enumerate(nums):
                t = target - num
                if t in nums_map:
                    del nums[i]
                    del nums[nums_map[t]]
                    return twoSum(nums, target, res+[[num, t]])
                nums_map[num] = i
            return res
        
        for i, num in enumerate(nums):
            curr_two_res = twoSum(nums[i+1:], -num, [])
            if len(curr_two_res) == 0:
                continue
            # list of sorted tuple       
            res.update([tuple(sorted(cand+[num])) for cand in curr_two_res])
        return [list(tup) for tup in res]