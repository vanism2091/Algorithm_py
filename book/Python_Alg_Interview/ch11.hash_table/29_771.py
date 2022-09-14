import collections
from typing import *
# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # book sol_4: 파이썬다운 방식
        return sum(s in jewels for s in stones)
        
        # book sol_3: Counter로 계산 생략
        freqs = collections.Counter(stones)
        count = 0

        for char in J:
            count += freqs[char]
        
        return count


        # book sol_2: defaultdict를 이용한 비교 생략
        freqs = collections.defaultdict(int)
        count = 0

        # 비교 없이 돌 빈도수 계산
        for char in stones:
            freqs[char] += 1

        # 비교 없이 보석 빈도수 합산
        for char in jewels:
            count += freqs[char]

        return count
        

        # book sol_1: using Hash Table (basic)
        freqs = {}
        count = 0

        for char in stones:
            freqs[char] = 1 if char not in freqs else freqs[char] + 1
        
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count

        # mine 2. counter 이용 
        having = collections.Counter(stones)
        return sum([having[jewel] for jewel in jewels])



        # mine 1. 사전 이용하기
        having = collections.defaultdict(int)
        for stone in stones:
            having[stone] += 1
        return sum([having[jewel] for jewel in jewels])
