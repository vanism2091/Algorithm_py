
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
테스트 1 〉	통과 (1.70ms, 10.4MB)
테스트 2 〉	통과 (247.38ms, 23MB)
테스트 3 〉	통과 (0.18ms, 10.2MB)
테스트 4 〉	통과 (4.31ms, 10.2MB)
테스트 5 〉	통과 (1.92ms, 10.3MB)
테스트 6 〉	통과 (1.76ms, 10.4MB)
테스트 7 〉	통과 (482.54ms, 23.8MB)
테스트 8 〉	통과 (462.79ms, 23.3MB)
테스트 9 〉	통과 (422.66ms, 23MB)
테스트 10 〉	통과 (1082.37ms, 25.4MB)
테스트 11 〉	통과 (1064.36ms, 25.4MB)

2진수로 바꿨을 때, 첫 0이 나오는 자리를 2**n 라고 하자.
그러면 주어진 x에 2**(n-1) 을 더하면 답이다.
1차는 array로 했는데, 
이 문제를 비트 연산을 활용해서 해결하는 방법이 있을까?
"""
# 2개 이하로 다른 비트
# https://school.programmers.co.kr/learn/courses/30/lessons/77885?language=python3
def solution(numbers):
    answer = [ f(x) for x in numbers ]
    return answer

def f(x:int):
    stack = list(map(int, bin(x)[2:]))
    idx = len(stack) - 2
    
    if sum(stack) == len(stack):
        return x + 2 ** (len(stack) - 1)
    elif stack[-1] == 0:
        return x + 1

    while idx >= 0:
        if stack[idx] == 0:
            return x + 2 ** (len(stack) - idx - 2)
        idx -= 1

examples = [[[2, 7], [3, 11]]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/77885/solution_groups?language=python3
def others():
    pass



