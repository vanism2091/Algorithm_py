
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
스파이들은 매일 다른 옷을 조합해 입어서 자신을 위장함.
전날과 같은 날 복장을 입으면 안됨. 종류: 얼굴, 상의, 하의, 겉옷
서로 다른 옷의 조합의 수를 return
- len(clothes): [1, 30]
- clothes_i: [의상 이름, 의상 종류]
- 의상의 이름은 유니크함
- 모든 문자열에 대해, 길이: [1, 20], 구성: 알파벳 소문자 + '_'
- 스파이는 하루에 최소 한 개의 의상을 입음

e.g.
input:
[   ["yellow_hat", "headgear"], 
    ["blue_sunglasses", "eyewear"], 
    ["green_turban", "headgear"]    ]
output:
5

이해:
헤드기어는 2개 있다. 동시에 사용 불가능하다. List: [1, 2]
eyewear은 1개 있다. 
둘 중 하나는 반드시 착용해야 한다. 00은 없다.
전자를 헤드기어, 후자를 아이웨어라고 하자.
10 20 01 11 21 : 5가지 방법

해결:
우선 의상의 종류를 해시 함수로, 해시맵을 만든다.
의상의 종류가 n개라면,
1개만 입는 방법: 종류별 원소를 곱함
2개 입는 방법: 종류 중 2개의 조합으로 원소 갯수 곱하기
...
n개를 입는 방법 : 모든 종류의 원소 갯수 곱하기

풀기 위해 해야 하는 것
1. 해시맵 만들기
2. keys()에서 1부터 n까지 조합 구하기. from itertools import combinations
3. 1..n for문 돌면서 각 조합의 원소 갯수 곱한걸 res에 더해준다.
"""
# 위장
# https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3

from itertools import combinations
import math
def solution_1(clothes):
    answer = 0
    # 1. 해시맵 만들기
    c_dict = {} 
    for c_name, c_type in clothes:
        if c_type in c_dict:
            c_dict[c_type].append(c_name)
        else:
            c_dict[c_type] = [c_name]

    # 2. combination
    def get_cnt_num(arr, num):
        cnt = 0
        for comb in combinations(arr, num):
            c_len = [len(c_dict[type]) for type in comb]
            cnt += math.prod(c_len)
        return cnt

    for i in range(1, len(c_dict)+1):
        answer += get_cnt_num(c_dict.keys(), i)

    return answer

"""
입은 수의 조합을 구하는 것이 아니라,
입을 수 있는 수 + 안입었을때 : 이 상태에서 n+1의 조합을 구하면 됨...
간단한 수학이네 ㅋㅋㅋㅋ..하 수학 공부하자
"""
def solution(clothes):
    # 질문하기 참고 후 다시 풀어봄
    c_dict = {}
    for _, ctype in clothes:
        c_dict[ctype] = c_dict[ctype]+1 if ctype in c_dict else 2
    return math.prod(c_dict.values()) - 1

examples = [[[['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']], 5], [[['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']], 3]]

test_cases(solution, examples)


"""
내가 dict로 구현한 카운터를 말그대로 카운터로 함 - 깔끔쓰
reduce 안쓰고 math.prod 써도 깔끔할듯. 물론 prod가 최신 문법이긴함(3.8이상)
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42578/solution_groups?language=python3
def others():
    def other_42578(clothes):
        from collections import Counter
        from functools import reduce
        cnt = Counter([kind for _, kind in clothes])
        answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
        return answer



