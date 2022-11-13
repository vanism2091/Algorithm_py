import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
모든 트럭이 다리를 지나려면, 최소 몇 초가 걸릴까?

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	실패 (0.25ms, 10.2MB)
테스트 5 〉	실패 (0.49ms, 10.2MB)
테스트 6 〉	실패 (0.39ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	실패 (0.40ms, 10.4MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
채점 결과
정확성: 71.4
합계: 71.4 / 100.0
"""

from collections import deque


# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
def solution_1(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    on_bridge = deque([])
    when_bridge = deque([])
    while trucks:
        if when_bridge and when_bridge[0] == answer - bridge_length + 1:
            on_bridge.popleft()
            when_bridge.popleft()
        while trucks and weight >= sum(on_bridge) + trucks[0]:
            answer += 1
            on_bridge.append(trucks.popleft())
            when_bridge.append(answer)
        answer = bridge_length + when_bridge[0] - 1
        pass
    answer = bridge_length + when_bridge[-1]     
    return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    on_bridge = deque([])
    when_bridge = deque([])
    while trucks:
        if when_bridge:
            on_bridge.popleft()
            when_bridge.popleft()
        print(when_bridge, weight, sum(on_bridge) + trucks[0])
        while trucks and weight >= sum(on_bridge) + trucks[0]:
            answer += 1
            on_bridge.append(trucks.popleft())
            when_bridge.append(answer)
        answer = bridge_length + when_bridge[0] - 1
    answer = bridge_length + when_bridge[-1]
    return answer

# examples = [[2, 10, [7, 4, 5, 6], 8], [100, 100, [10], 101], [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 110]]
examples = [[20, 10, [7, 4, 5, 6], 62], [100, 30, [10, 10, 10, 10, 10, 10, 10, 10, 20], 401]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42583/solution_groups?language=python3
def others():
    pass



