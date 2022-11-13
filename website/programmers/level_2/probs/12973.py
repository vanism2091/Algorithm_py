import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
1. 같은 알파벳이 2개 붙어있는 짝을 찾는다.
2. 그 둘을 제거한 뒤 앞뒤로 문자열을 이어붙인다.
3. 1번 과정을 반복한다.
4. 문자열이 모두 제거되면, 짝지어 제거하기가 종료된다.

문자열이 주어졌을 때, 이를 성공적으로 수행할 수 있는지 반환하는 함수를 완성하라

constraint
- 문자열 길이 1_000_000
- 문자열은 모두 소문자

re를 쓸 수 있으면 좋을 것 같음. 가령,
같은 알파벳 딱 2개로 이어진 것들을 찾아내서, 다 지우고 나머지 붙이는 식으로.
그런데 그러는 과정에서 실패하는 경우, 예외 케이스가 있을까?

baaabbab -> baab -> bb -> 0
abccbbacbbcabaabba -> abaccabbba -> abaaba -> abba -> aa -> 0
일단 찾아보고 구현해본 후 안되면 문제대로 앞에서 찾아보는 식으로 해보자.
re split 은 패턴으로 분리하는 메소드임.
"""
import re
# 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=python3
def solution_1(s):
    pattern = "|".join([f'[{chr(i)}]{{2}}' for i in range(ord('a'), ord('z')+1)])
    new_str = re.sub(pattern, "", s)
    if not new_str:
        return 1
    while s != new_str:
        s = new_str
        new_str = re.sub(pattern, "", s)
    return 0 if s else 1

"""
아름답게 시간초과 나는 코드 :)...
투포인터를 써보자
1. 문자열을 리스트로 만들기
2. 리스트를 돌면서, 직전 인덱스와 다음 인덱스의 값이 같다면 둘을 "" 로 치환 ㄴㄴ
3. 문자열 반환
4. 재귀로

말그대로 찐 투포인터 쓰면 될듯
-read_idx
-write_idx

7
abbcbbca

a
1, 1
ac 3, 1 -> 2
4, 2일때, bb로 같음
6, 2 c != a
acc 7, 3
acca # while문 이후, 남은 a를 쓸 로직이 필요

bbcbbcaa
2,0
c / 3, 1
c / 5, 1
cc / 6, 2
read_idx == 8 <
read_idx == len(s_li) > 마지막이 같음(빼야함)
    != > 마지막 문자열도 포함해야 함.

이것도 시간초과 :)
정확성: 30.3
효율성: 5.0
합계: 35.3 / 100.0
"""


def solution_2(s):
    if len(s) % 2:
        return 0
    def get_rid_of_couples(s_li):
        read_idx, write_idx = 0, 0
        while read_idx < len(s_li)-1:
            if s_li[read_idx] != s_li[read_idx+1]:
                s_li[write_idx] = s_li[read_idx]
                write_idx += 1
                read_idx += 1
            else:
                read_idx += 2
        new_li = s_li[:write_idx]
        if read_idx != len(s_li):
            new_li.append(s_li[-1])
        return new_li
    
    li_string = list(s)
    while li_string:
        new_list = get_rid_of_couples(li_string)
        if li_string == new_list:
            return 0
        li_string = new_list
    return 1


"""
deque를 사용하자 :)
다 통과함 엉엉....
"""
from collections import deque
def solution(s):
    sq = deque(list(s[1:]))
    stack = [s[0]]
    while sq:
        left = stack.pop()
        right = sq.popleft()
        if left == right:
            if not sq:
                return 0 if stack else 1
            if not stack:
                stack.append(sq.popleft())
        else:
            stack.extend([left, right])
    return 0 if stack else 1

examples = [['baabaa', 1], ['cdcd', 0]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12973/solution_groups?language=python3
def others():
    def solution(s):
        answer = []
        for i in s:
            if not(answer):
                answer.append(i)
            else:
                if(answer[-1] == i):
                    answer.pop()
                else:
                    answer.append(i)    
        return not(answer)



