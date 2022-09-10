"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

- Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

- Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

- Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        # sol_2: stack
        stack = []
        volume = 0
        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼냄
                top = stack.pop()
                if not len(stack):
                    break
            
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)
        return volume


        # sol_1: two pointer
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

        
        
        # mine
        max_height = max(height)
        res, left, right = 0, 0, len(height) - 1
        curr_height = height[left]
        while height[left] != max_height:
            curr_height = max(height[left], curr_height)
            res += curr_height-height[left]
            left += 1
        
        curr_height = height[right]
        while height[right] != max_height:
            curr_height = max(height[right], curr_height)
            res += curr_height-height[right]
            right -= 1

        res += max_height*(right-left) - (height[left+1: right])
        return res
        
        
        