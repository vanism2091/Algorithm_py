
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases

"""
1. 십진수를 2진수로 바꿈 

1개일 때,
1       1
10      2
100     4

2개일 때
11      3
101     5
110     6
1001    9
1010    10
1100    12

3개일 때
111     7
1011    11
1101    13
1110    14

1001110
1010011
1010110

1111000

10000111

숫자를 하나씩 늘리면서 1이 몇개인지를 체크
"""
# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911?language=python3
def solution(n):
    num_one = bin(n).replace("0b", "").count('1')
    is_next = False
    while not is_next:
        n += 1
        curr = bin(n).replace("0b", "")
        if curr.count('1') == num_one:
            is_next = True
    return int(curr,2)

examples = [[78, 83], [15, 23]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12911/solution_groups?language=python3
def others():
    def nextBigNumber(n, count = 0):
        return n if bin(n).count("1") is count else nextBigNumber(n+1, bin(n).count("1") if count is 0 else count)



