
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
아까전에 이걸 cnt하는걸로 구현한 사람이 있어서
그 방식으로 한 번 해보자.
() 종류가 1개이기 때문에 굳이 스택을 쓸 필요가 없음
( 일때는 cnt를 1 더하고 
) 일때는 cnt를 1 뺌
cnt가 도중에 음수가 나오면 False, cnt가 최종적으로 0이 아니면 False
"""
# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
def solution(s):
    if len(s) % 2: return False
    cnt = 0
    for b in s:
        cnt = cnt+1 if b == '(' else cnt-1
        if cnt < 0: return False
    return False if cnt else True

examples = [['()()', True], ['(())()', True], [')()(', False], ['(()(', False]]

test_cases(solution, examples)

"""
이 코드는 (, ) 말고 다른 글자가 포함된 경우의 괄호 맞는지 확인하는 거. 문제가 약간 바꼈나봄
return x == 0 오.. 찢었다..!
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12909/solution_groups?language=python3
def others():
    def is_pair(s):
        x = 0
        for w in s:
            if x < 0:
                break
            x = x+1 if w=="(" else x-1 if w==")" else x
        return x==0



