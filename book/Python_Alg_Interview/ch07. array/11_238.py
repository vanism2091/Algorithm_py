from typing import *

# https://leetcode.com/problems/product-of-array-except-self/
"""
Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # sol_1-book 책 코드 에서 다른 코드 보고 약간 수정
        # 아래랑 다를게 없는데 얘는 559네? 음.. 복불복인듯...
        out = [1] * len(nums)
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out[i] *= p
            p *= nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] *= p
            p *= nums[i]
        return out

        ## 다른 코드 219ms
        prefix = 1
        postfix = 1
        res = [1] * len(nums)
        
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res

        ## sol_1-book 책 코드
        # 공간 복잡도 O(1)
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p* nums[i]
        return out
        
        # sol_1 - 책 읽고 내가 해보기
        # 공간복잡도가 O(n)
        from_left = [1 for _ in range(len(nums))]
        from_right = from_left[:]
        for i in range(len(nums)-1):
            from_left[i+1] = from_left[i] * nums[i]
            from_right[i+1] = from_right[i] * nums[-(i+1)]
        return [l*r for l, r in zip(from_left, from_right[::-1])]