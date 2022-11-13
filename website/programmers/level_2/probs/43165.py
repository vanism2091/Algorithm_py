
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
input:
    nums: 자연수 숫자들 
        len(nums): [2, 20]
        nums_i: [1, 50]
    target#: [1, 1000] 만들어야 하는 숫자
nums를 적절히 조합해서 target 만드는 방법의 수 구하기

카운터를 사용하자.
문제는 DFS, BFS 쓰라는데 이거 어케 했더라 :)ㅋㅋㅋㅋㅋㅋ
트리를 생각해
         1
      +1   -1
    +1 -1 +1 -1 이런 느낌?
최종 답이 target이면 cnt += 1
(current, last_sum) nums를 돌면서 하나씩 넣고 빼고.., queue 쓰자
nums에서 1개 빼면,
queue가 빌때까지 
    la, ll_sum = queue.popleft()
    queue.append((+curr, la+ll_sum)) 
    queue.append((-curr, la+ll_sum))
nums를 다 돌았으면,
queue를 하나씩 뽑으면서,
curr + last_sum == target일 때, cnt += 1
"""
# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(0,0)])
    for num in numbers:
        for _ in range(len(q)):
            prev_num, ll_sum = q.popleft()
            q.extend([(+num, prev_num+ll_sum), (-num, prev_num+ll_sum)])
    while q:
        curr, last_sum = q.pop()
        if curr+last_sum == target:
            answer += 1
    return answer

examples = [[[1, 1, 1, 1, 1], 3, 5], [[4, 1, 2, 1], 4, 2]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/43165/solution_groups?language=python3
def others():
    def other_43165(numbers, target):
        ## 재귀로 품
        def solution(numbers, target):
            if not numbers and target == 0 :
                return 1
            elif not numbers:
                return 0
            else:
                return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])






