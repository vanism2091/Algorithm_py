from typing import *
# https://leetcode.com/problems/valid-parentheses/

"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # sol_1 stack 일치 여부 판별
        # - 매핑 테이블 만들기
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

        
        # mine
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if not stack:
                    return False
                op = stack.pop()
                if abs(ord(c) - ord(op)) > 2:
                    return False
        return not bool(stack)