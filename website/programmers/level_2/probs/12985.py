
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
참가자 수 N.
나 A, 경쟁자 B 
나는 B와 몇 번째 라운드에서 만날까?
4, 7 -> 3
2nd
    4+1//2 : 2
    7+1//2 : 4
3rd
    2+1//2 : 1
    5//2    : 2
만났음 :)
4, 9는?
2, 1, 1
5, 3, 2

15
39
8, 4, 2, 1, 1
20, 10, 5, 3, 2

27 39
14 7 4 2 1
20 10 5 3 2

그래봤자 20번 이하임. 일단 걍 그대로 구현하자.
"""
# 예상 대진표
# https://school.programmers.co.kr/learn/courses/30/lessons/12985?language=python3
import math
def solution(n,a,b):
    m, M = min(a,b), max(a, b)
    if M - m == 1 and m % 2:
        return 1
    for i in range(2, int(math.log2(n))+1):
        m, M = (m+1)//2, (M+1)//2
        if M - m == 1 and m % 2:
            return i



examples = [[8, 4, 7, 3]]

test_cases(solution, examples)

"""

a, b 를 xor 취하는 과정에서 ab 사이의 거리가 가까우면 상위비트는 차이가 나지 않겠죠? 거꾸로 ab 사이의 거리가 멀면 상위비트가 차이 날 거고요. 그래서 xor 연산 결과의 길이를 리턴해주면 라운드가 나오는 아이디어인것으로 보여요.

1을 빼는 것은 선수의 위치를 0-index 형태로 바꾸기 위함인 것 같고요.
a, b는 각각 선수의 위치이고 이를 2비트 수로 표현했을 때a, b가 인접한 위치로 가려면, 두 비트가 같을 때는 0을 더하고 두 비트가 다를 때는 1을 더하는 XOR 연산으로 생각할 수 있겠네요.
토너먼트 트리를 그렸을 때, 윗단을 최상위 비트, 아래단을 최하위 비트로 생각하면 이해되실 것 같네요. 가령, 5(101)의 가장 앞의 비트값(최상위)가 트리의 꼭대기




"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12985/solution_groups?language=python3
def others():
    def solution(n,a,b):
        return ((a-1)^(b-1)).bit_length()



