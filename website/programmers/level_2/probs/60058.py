
import os
import sys

from sympy import Q
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
균형잡힌 괄호 문자열: (와 )의 갯수가 같다.
올바른 괄호 문자열: 균형잡힌 괄호 문자열이면서 괄호의 짝이 모두 맞다

균형잡힌 괄호 문자열을 올바른 괄호 문자열로 변환하는 방법
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.

균형잡힌 괄호 문자열이 주어졌을 때, 위를 수행해서 올바른 괄호 문자열로 바꾸어 return

위에 설명된 알고리즘을 그대로 구현할 수 있으면 되겠다.
e.g. 
input (()))(
    1. 2) (()) | )(
"""
# 괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3
def solution(p):
    def is_sound_bracket(s):
        check = []
        for b in s:
            if b == '(':
                check.append('(')
            else:
                if not check:
                    return False
                check.pop()
        if check:
            return False
        return True
    
    def get_b_index(s):
        o, c, i = 0, 0, 0
        for b in s:
            if b == '(':
                o += 1
            else:
                c += 1
            i += 1
            if o == c:
                return i

    def make_sound_bracket(s):
        # 1.
        if not s:
            return s
        # 2.
        v_idx = get_b_index(s)
        u, v = s[:v_idx], s[v_idx:]
        if is_sound_bracket(u):
            return u + make_sound_bracket(v)
        else:
            return '(' + make_sound_bracket(v) + ')' + "".join(['(' if b ==')' else ')' for b in u[1:-1]])
    return p if is_sound_bracket(p) else make_sound_bracket(p)

"""
1트 이후에 12번 이후부터 틀리길래 뭐지 했는데,
4-4에서 문자열을 역순으로 뒤집은걸로 착각해서 틀린 것이었다. 괄호 방향을 뒤집는게 맞음... 아.. ㅋ..
문제를 제대로 읽자 :):):):)
"""


# examples = [['))()((', '()()()']]
examples = [['(()())()', '(()())()'], [')(', '()'], ['()))((()', '()(())()']]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/60058/solution_groups?language=python3
def others():
    def solution(p):
        if p=='': return p
        r=True; c=0
        for i in range(len(p)):
            if p[i]=='(': c-=1
            else: c+=1
            if c>0: r=False
            if c==0:
                if r:
                    return p[:i+1]+solution(p[i+1:])
                else:
                    return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))


def others_2():
    def solution(p):
        u, v = [], []
        if correct(p): return p
        for i in range(2, len(p)+1,2):
            if balanced(p[:i]):
                u, v = p[:i], p[i:]
                break
        if correct(u): return u + solution(v)
        else:
            print(u)
            print(u[1:len(u)-1].replace('(','0').replace(')','(').replace('0',')'))
            return '(' + solution(v) + ')' + u[1:len(u)-1].replace('(','0').replace(')','(').replace('0',')')


    def balanced(b): return b.count('(') == b.count(')')


    def correct(c):
        cnt = 0
        for i in range(len(c)):
            cnt = cnt + 1 if c[i] == '(' else cnt - 1
            if cnt < 0: return False
        return True
