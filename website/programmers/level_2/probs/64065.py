
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
n개의 요소를 가진 n-튜플
튜플의 성질 
- 중복된 원소가 있을 수 있음
- 원소에 정해진 순서가 있고, 순서가 다르면 서로 다른 튜플임
- 튜플의 원소 개수는 유한함

원소의 개수가 n개이고, 중복되는 원소가 없는 튜플이 주어진다.
이를 다음 집합 기호로 표현할 수 있다.
"{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}"
그리고 다음과 동일하다.
{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}

튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때,
s가 표현하는 튜플을 배열에 담아 return하라

constraint
    - s의 길이 [5, 1_000_000]
    - s = ['{' | '}' | [0-9] | ,]
    - 숫자가 0으로 시작하는 경우는 없다
    - s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있다
    - s가 표현하는 튜플의 원소 자연수[1, 100_000]
    - return하는 배열의 길이는 500 이하이다.

생각해보기
-> 문자열의 [2:-2]에 대해 "},{"을 "|"로 치환 후 split.
"""
import ast
# 튜플
# https://school.programmers.co.kr/learn/courses/30/lessons/64065?language=python3
def solution(s):
    li = list(map(lambda x: ast.literal_eval(f'{{{x}}}'), s[2:-2].split("},{")))
    li.sort(key=lambda x:len(x))
    for i in range(len(li)-1, 0, -1):
        li[i] -= li[i-1]
    return [int(list(x)[0]) for x in li]

examples = [['{{2},{2,1},{2,1,3},{2,1,3,4}}', [2, 1, 3, 4]], ['{{1,2,3},{2,1},{1,2,4,3},{2}}', [2, 1, 3, 4]], ['{{20,111},{111}}', [111, 20]], ['{{123}}', [123]], ['{{4,2,3},{3},{2,3,4,1},{2,3}}', [3, 2, 4, 1]]]

test_cases(solution, examples)

"""
1. s에서 모든 숫자를 찾아서, 숫자를 카운트함
    많이 있는 숫자부터 반환
2; eval('[1,2,3]') -> [1,2,3]
    와우 처음 알았음
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/64065/solution_groups?language=python3
def others():
    def solution(s):

        s = Counter(re.findall('\d+', s))
        return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

    import re
    from collections import Counter


    def solution(s):
        s = eval(s.replace("{", "[").replace("}", "]"))
        answer = list({num:0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
        return answer

