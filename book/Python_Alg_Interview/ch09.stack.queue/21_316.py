import collections
from typing import *
# https://leetcode.com/problems/remove-duplicate-letters/
"""
316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Input: s = "bcabc"
Output: "abc"
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # sol_2-book: stack
        seen, stack, counter = set(), [], collections.Counter(s)
        
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)
        
        # sol_1-book: recursive
        # set으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할 때 분리
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''