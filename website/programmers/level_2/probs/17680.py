
import os
import sys

from numpy import size
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

heapq를 써보고 싶어서 :) 근데 2개 실패함.. :(  -> 0일때 정의

채점 결과
정확성: 90.0
합계: 90.0 / 100.0
"""
# [1차] 캐시
import itertools
import heapq
# https://school.programmers.co.kr/learn/courses/30/lessons/17680?language=python3
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    class Cache:
        def __init__(self, size) -> None:
            self.size = size
            self.pq = []
            self.entry_finder = {}
            self.REMOVED = '<removed>'
            self.counter = itertools.count()
            self.curr_entities = 0
        
        def add_location(self, location):
            if location in self.entry_finder:
                self.remove_location(location)
            elif self.curr_entities == self.size:
                self.pop_location()
            self.count = next(self.counter)
            self.curr_entities += 1
            entry = [self.count, location]
            self.entry_finder[location] = entry
            heapq.heappush(self.pq, entry)
            self.is_full = len(self.pq) == self.size

        def remove_location(self, location):
            entry = self.entry_finder.pop(location)
            entry[-1] = self.REMOVED
            self.curr_entities -= 1

        def pop_location(self):
            while self.pq:
                cnt, location = heapq.heappop(self.pq)
                if location is not self.REMOVED:
                    del self.entry_finder[location]
                    self.curr_entities -= 1
                    return location
        
        def find_location(self, location):
            return location in self.entry_finder
    cache = Cache(cacheSize)
    answer = 0
    for city in map(lambda x: x.lower(), cities):
        answer += 1 if cache.find_location(city) else 5
        cache.add_location(city)
    return answer

# examples = [[3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'], 50], [3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'], 21], [2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'], 60], [5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'], 52], [2, ['Jeju', 'Pangyo', 'NewYork', 'newyork'], 16], [0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'], 25]]
examples = [[4, ["1", "2", "3", "4", "2"], 21],]
test_cases(solution, examples)

"""
deque(maxlen=cacheSize)
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/17680/solution_groups?language=python3
def others():
    def solution(cacheSize, cities):
        import collections
        cache = collections.deque(maxlen=cacheSize)
        time = 0
        for i in cities:
            s = i.lower()
            if s in cache:
                cache.remove(s)
                cache.append(s)
                time += 1
            else:
                cache.append(s)
                time += 5
        return time



