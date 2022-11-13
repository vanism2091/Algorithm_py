
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

"""
# 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3
def solution(s):
    min_len = len(s)
    for i in range(1, len(s)//2+1):
        s_li = []
        for j in range(0, len(s)//i+1):
            start, end = i*j, i*(j+1)
            if end > len(s):
                end = len(s)
            s_li.append(s[start:end])
        cnt = 1
        prev = s_li[0]
        res_li = []
        for sub_s in s_li[1:]:
            if prev == sub_s:
                cnt += 1
            else:
                res_li.append(str(cnt)+prev if cnt != 1 else prev)
                cnt = 1
                prev = sub_s
        res_li.append(str(cnt)+prev if cnt != 1 else prev)
        res = len(''.join(res_li))
        min_len = min(res, min_len)
    return min_len

examples = [['aabbaccc', 7], ['ababcdcdababcdcd', 9], ['abcabcdede', 8], ['abcabcabcabcdededededede', 14], ['xababcdcdababcdcd', 17]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/60057/solution_groups?language=python3
def others():
    pass



