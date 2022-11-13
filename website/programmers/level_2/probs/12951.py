
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

실패 이유: 공백 문자가 연속해서 나올 수 있음
굳이.. :)
"""
# JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=python3
def solution(s):
    answer = []
    is_head = True
    for c in s:
        if c == ' ':
            is_head = True
            answer.append(c)
        else:
            if is_head:
                answer.append(c.upper())
                is_head = False
            else:
                answer.append(c.lower())
    return "".join(answer)

examples = [['3people    unFollowed me', '3people    Unfollowed Me']]
# examples = [['3people unFollowed me', '3people Unfollowed Me'], ['for the last week', 'For The Last Week']]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12951/solution_groups?language=python3
def others():
    pass



