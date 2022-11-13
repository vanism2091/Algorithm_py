from typing import *
import datetime
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
참고한 링크
https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python

1. str -> time
    1) rfind: 오른쪽에서부터 찾기
        https://docs.python.org/3/library/stdtypes.html?highlight=rfind#str.rfind
2. start, end 구하기
3. end 기준으로 max 체크

첫 시도

채점 결과
정확성: 81.8
합계: 81.8 / 100.0
까비... 반례가 뭘까?

이전 로그의 끝과 동떨어진 친구라면 자동으로 True가 되지 않음.
따라서 현재 개수 구할 때 True로 바꿔준다.

채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""
# [1차] 추석 트래픽
# https://school.programmers.co.kr/learn/courses/30/lessons/17676?language=python3
def solution(lines):
    answer = 0
    d_tuples = [to_datetime_tuple(s) for s in lines]
    check = [True] + [False] * (len(lines) - 1)
    total_len = len(lines)
    for i in range(total_len):
        # true로 변경
        start = d_tuples[i][1]
        end = start + datetime.timedelta(seconds=0.999)
        # 2번째 시도에 추가한 단 한 줄... :)
        check[i] = True
        for j in range(i+1, total_len):
            if check[j]:
                continue
            if d_tuples[j][0] <= end:
                check[j] = True 
        # true 개수세기
        answer = max(answer, sum(check))
        # false로 변경
        check[i] = False
    return answer

def to_datetime_tuple(s:str):
    i = s.rfind(" ")
    t, sec = s[:i], float(s[i+1: -1]) - 0.001
    end = datetime.datetime.fromisoformat(t)
    start = end - datetime.timedelta(seconds=sec)
    return (start, end)

examples = [[[
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
], 7], [[
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
], 2], [[
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
], 1]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/17676/solution_groups?language=python3
def others():
    pass

