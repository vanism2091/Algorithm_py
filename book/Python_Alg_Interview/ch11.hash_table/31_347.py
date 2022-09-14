import collections
import heapq
from typing import *

# https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sol_2-book : pythonic
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

        # sol_1-book : Counter를 이용한 음수 순 추출
        # - 요소의 값을 키로 하는 해시 테이블을 만들고, 빈도수 저장
        # - 우선순위 큐를 이용해 k번만큼 추출
        # - 책에서는 heapq를 이용해 풀이할 것. 내가 먼저 한 번 해보자.
        # 파이썬 heapq 모듈은 min heap만 지원하므로 freq를 음수로 변환
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        
        topk = list()
        # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk
        

        # use walus expression
        # https://stackoverflow.com/questions/10291997/how-can-i-do-assignments-in-a-list-comprehension
        # use walrus operator
        counter = collections.Counter(nums)
        hq = [(-counter[num], num) for num in counter]
        heapq.heapify(hq)
        return [num[1] for _ in range(k) if (num := heapq.heappop(hq))]

        
        counter = collections.Counter(nums)
        hq = [(-counter[num], num) for num in counter]
        heapq.heapify(hq)
        res = [0] * k
        for i in range(k):
            res[i] = heapq.heappop(hq)[1]
        return res
        
        
        # mine: Counter
        return [num for num, _ in collections.Counter(nums).most_common(k)]

        # mine: Counter 없이?
        # dictionary에 1개씩 넣고, key: num, val: freq.
        # sort 후 상위 k개 num 출력
        # 문제에서 요구한게 O(n log n) 보다 좋아야 함.. 이므로 sorted는 ㄴㄴ
        freqs = collections.defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        return [num for num, _ in sorted(freqs.items(), key=lambda x: x[1])[:k]]
