import collections
from curses.ascii import isalnum
import re
from typing import *

# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # mine_after
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        stack = collections.deque(s)
        while len(stack) > 1:
            if stack.popleft() != stack.pop():
                return False
        return True
        

        # sol
        s = s.lower()
        # use regular expression
        s = re.sub("[^a-z0-9]", "", s)
        
        return s == s[::-1] 
        
        """
        2nd
        - isalnum
        - use pop, popleft
        """
        strs:Deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True
        
        
        """
        1st (mine)
        """
        strs = []
        for char in s:
            if char.isalpha():
                strs.append(char.lower())
            elif char.isdigit():
                strs.append(char)
        
        # return True if strs == strs[::-1] else False
        return strs == strs[::-1]