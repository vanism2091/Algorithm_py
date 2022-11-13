
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
같은 길이의 자연수 배열 A, 배열 B
배열의 길이만큼
    - A, B에서 한 개의 숫자를 뽑아 두 수를 곱함
    - 그 곱의 누적합: 최소로 만드는 것이 목표
sort 후에 작은수 * 큰수 하면 될듯
"""
# 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941?language=python3
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

examples = [[[1, 4, 2], [5, 4, 4], 29], [[1, 2], [3, 4], 10]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12941/solution_groups?language=python3
def others():
    def getMinSum(A,B):
        return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
    



