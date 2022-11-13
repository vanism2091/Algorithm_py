
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

"""
# 행렬의 곱셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12949?language=python3
def solution(arr1, arr2):
    m, n, l = len(arr1), len(arr2[0]), len(arr2)
    answer = [[] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            res = 0
            for k in range(l):
                res += arr1[i][k] * arr2[k][j]
            answer[i].append(res)
    return answer

examples = [[[[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]], [[15, 15], [15, 15], [15, 15]]], [[[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]], [[22, 22, 11], [36, 28, 18], [29, 20, 14]]]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12949/solution_groups?language=python3
def others():
    def productMatrix(A, B):
        return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]



