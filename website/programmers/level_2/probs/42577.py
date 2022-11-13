
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

"""
# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3
def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        # if phone_book[i] in phone_book[i+1]:
        #   포함이 아니라 '접두어'여야함
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer

examples = [[['119', '97674223', '1195524421'], False], [['123', '456', '789'], True], [['12', '123', '1235', '567', '88'], False]]

test_cases(solution, examples)

"""
아래와 또 다른 풀이. startwith

해쉬를 이용한 풀이를 내가 먼저 생각해보고 아래 코드를 보자.
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42577/solution_groups?language=python3
def others():
    def other_42577(phone_book):
        answer = True
        hash_map = {}
        for phone_number in phone_book:
            hash_map[phone_number] = 1
        for phone_number in phone_book:
            temp = ""
            for number in phone_number:
                temp += number
                if temp in hash_map and temp != phone_number:
                    answer = False
        return answer



