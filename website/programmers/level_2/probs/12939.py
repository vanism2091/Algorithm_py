
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
으음..? 갓이썬 문제 하하하..
input을 split 후에 map int 로 정수 리스트로 만든 후
max, min을 취한 후에 다시 문자열로 바꾼다.
"""
# 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3
def solution(s):
    l = list(map(int, s.split()))
    # m, M = min(l), max(l)
    # return f'{m} {M}'
    return f'{min(l)} {max(l)}'

examples = [['1 2 3 4', '1 4'], ['-1 -2 -3 -4', '-4 -1'], ['-1 -1', '-1 -1']]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12939/solution_groups?language=python3
def others():
    def solution(s):
        s = list(map(int,s.split()))
        return str(min(s)) + " " + str(max(s))



