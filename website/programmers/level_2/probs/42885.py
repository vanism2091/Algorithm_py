
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
GREEDY
1. 소팅한다. 제일 큰 수 뽑고, 제일 작은 수를 확인해서 추가가능하면 추가하고, 그렇지 않으면 뽑는다.
2. deque를 쓰자. 작을 때, popleft해야 하니까.
"""
from collections import deque
# 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885?language=python3
def solution(people, limit):
    answer = 0
    pq = deque(sorted(people))
    while pq:
        curr = pq.pop()
        while pq and curr + pq[0] <= limit:
            curr += pq.popleft()
        answer += 1
    return answer

examples = [[[70, 50, 80, 50], 100, 3], [[70, 80, 50], 100, 3]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42885/solution_groups?language=python3
def others():
    def solution(people, limit) :
        answer = 0
        people.sort()

        a = 0
        b = len(people) - 1
        while a < b :
            if people[b] + people[a] <= limit :
                a += 1
                answer += 1
            b -= 1
        return len(people) - answer



