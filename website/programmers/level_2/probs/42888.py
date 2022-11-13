
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

"""
# 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888?language=python3
def solution(record):
    record = list(map(lambda x:x.split(), record))
    user_dict = {}
    text_dict = {
        "Enter": "님이 들어왔습니다.",
        "Leave": "님이 나갔습니다."
    }
    for rec in record:
        if rec[0] in ("Enter", "Change"):
            user_dict[rec[1]] = rec[2]
            
    return [user_dict[rec[1]]+text_dict[rec[0]] for rec in record if rec[0] in ("Enter", "Leave")]

examples = [[['Enter uid1234 Muzi', 'Enter uid4567 Prodo', 'Leave uid1234', 'Enter uid1234 Prodo', 'Change uid4567 Ryan'], ['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다.', 'Prodo님이 들어왔습니다.']]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42888/solution_groups?language=python3
def others():
    pass



