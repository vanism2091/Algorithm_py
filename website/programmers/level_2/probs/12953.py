
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
[4, 6, 8, 14]   168
2*2, 2*3, 2*2*2, 2*7
네 개의 공약수를 찾아서 n번 나누면 됨 ㄴㄴ
그냥 최소공배수, 최대 공약수 구현해서,
하나씩 최소공배수를 찾아갔음..
"""
import math
# N개의 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12953?language=python3
def solution(arr):
    def gcd(a, b):
        if a % b == 0:
            return b
        return gcd(b, a%b)
    def lcm(a, b): return a*b//gcd(a,b)
    mul = math.prod(arr)
    len_arr = len(arr)
    g = arr.pop()
    while arr:
        g = lcm(g, arr.pop())
    return g

examples = [[[4, 6, 8, 14], 168], [[1, 2, 3], 6]]

test_cases(solution, examples)

"""
나랑 같은데, Gcd를 모듈로 쓰심
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12953/solution_groups?language=python3
def others():
    from fractions import gcd
    def nlcm(num):
        answer = num[0]
        for n in num:
            answer = n * answer / gcd(n, answer)

        return answer



