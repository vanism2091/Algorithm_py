from my_utils import test_cases
import os
import sys
sys.path.insert(0, os.getcwd())
"""
res에 변환 점수 (4 - score 또는 score - 4) 를 더한 후
res를 돌면서 성격 유형으로 치환한다.
점수가 같다면 사전 순: 0점일 때 0번째 타입

아쉬운 점:
- "R", "C" 등을 하드코딩한 점
- if, elif, elif, elif문과 반복
"""
# 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3


def solution(survey, choices):
    res = [0, 0, 0, 0]
    types = ["RT", "CF", "JM", "AN"]
    for q, choice in zip(survey, choices):
        if "R" in q:
            res[0] += choice - 4 if q[0] == "R" else 4 - choice
        elif "C" in q:
            res[1] += choice - 4 if q[0] == "C" else 4 - choice
        elif "J" in q:
            res[2] += choice - 4 if q[0] == "J" else 4 - choice
        elif "A" in q:
            res[3] += choice - 4 if q[0] == "A" else 4 - choice

    for i in range(4):
        res[i] = types[i][0] if res[i] <= 0 else types[i][1]

    return ''.join(res)


examples = [[['AN', 'CF', 'MJ', 'RT', 'NA'], [5, 3, 2, 7, 5],
             'TCMA'], [['TR', 'RT', 'TR'], [7, 1, 3], 'RCJA']]

test_cases(solution, examples)

"""
아래 코드를 바탕으로 솔루션 바꿔봄
"""


def solution_2():
    def solution(survey, choices):
        type_dict = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
        for q, choice in zip(survey, choices):
            if q not in type_dict.keys():
                type_dict[q[::-1]] += 4 - choice
            else:
                type_dict[q] += choice - 4

        res = []
        for k, v in type_dict.items():
            res.append(k[0] if v <= 0 else k[1])

        return ''.join(res)


"""
참고하면 아쉬운 점을 개선할 수 있는 코드.
- "R", "C" 등을 하드코딩한 점
    - 유형을 dictionary의 key로
- if, elif, elif, elif문과 반복
    - 키가 아닌 유형은 반대로 정렬 - 키로 변환 후 점수 계산
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/118666/solution_groups?language=python3


def others():
    def solution(survey, choices):
        my_dict = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
        for A, B in zip(survey, choices):
            if A not in my_dict.keys():
                A = A[::-1]
                my_dict[A] -= B-4
            else:
                my_dict[A] += B-4

        result = ""
        for name in my_dict.keys():
            if my_dict[name] > 0:
                result += name[1]
            elif my_dict[name] < 0:
                result += name[0]
            else:
                result += sorted(name)[0]

        return result
    pass
