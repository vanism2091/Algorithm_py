from turtle import st
from typing import *
# https://leetcode.com/problems/daily-temperatures/

"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # sol_1: book
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer
        

        # sol_1 -b_mine (설명만 보고 코딩)
        # time limit ... 
        # - 1
        # stack, res = [], [0] * len(temperatures)
        # - 2
        # stack = []
        # res = [0] * len(temperatures)
        # 2일 때는 제한에 안걸렸지만 1일때는 왜인지 모르게 계속 시간 제한이 뜬다. 멀티 할당이 더 느린가?
        stack, res = [], [0] * len(temperatures)

        for i, cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

        # mine
        # time limit
        res, seen = [], []
        while temperatures:
            cur_day = 0
            cur_temp = temperatures.pop()
            for i in range(1,len(seen)+1):
                if seen[-i] > cur_temp:
                    cur_day = i
                    break
            res.append(cur_day)
            seen.append(cur_temp)
        return res[::-1]