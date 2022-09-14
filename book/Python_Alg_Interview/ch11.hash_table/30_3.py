import collections
from typing import *
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sol_1-book: 슬라이딩 윈도우와 투포인터로 사이즈 조절
        used = {}
        max_length, start = 0
        for index, char in enumerate(s):
            ### 윈도우 바깥의 문자는 예전에 등장했어도 무시한다. (left를 갱신할 때마다 max 취하는 것보다 이게 더 효율적인듯)
            # 이미 등장한 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char + 1] 
            else:   # 최대 부분 문자열 길이 갱신 
                max_length = max(max_length, index - start + 1)
            
            # 현재 문자의 위치 삽입
            used[char] = index
        
        return max_length

        # mine
        # n트만에 드디어 정답..
        if len(s) < 2:
            return len(s)
        
        check = {}
        left = 0
        len_max = 0

        for i, char in enumerate(s):
            if char in check:
                len_max = max(len_max, i - left)
                left = max(left, check[char]+1)
            check[char] = i
        return max(len_max, len(s)-left)


# def lengthOfLongestSubstring(s: str) -> int:
# lengthOfLongestSubstring("abba")