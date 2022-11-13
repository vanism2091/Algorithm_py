
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
진도가 100일 때 서비스 반영 가능
개발 속도는 모두 다르다. 
뒤에 있는 기능이 먼저 개발될 수 있고,
뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포된다.

input: 
    progresses: 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
    speeds: 작업의 개발 속도가 적힌 정수 배열
    - len(progress), len(speeds) : [0? 1?, 100]
    - progresses_i, speeds_i : [1, 100]
output:
    각 배포마다 몇 개의 기능이 배포되는지 적힌 배열

예제
progresses  |    speeds |   return
[93, 30, 55]    |   [1, 30, 5]  |   [2, 1]
[95, 90, 99, 99, 80, 99]    |   [1, 1, 1, 1, 1, 1]	|   [1, 3, 2]

# 1번 예제
[7일 후, 3, 9 ] -> [2, 1]
5,10,1,1,20,1 -> 1 3 2
"""
# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
import math
def solution(progresses, speeds):
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    
    answer = []
    cnt, curr_max = 1, days[0]
    for day in days[1:]:
        if curr_max < day:
            answer.append(cnt)
            cnt = 1
            curr_max = day
        else:
            cnt += 1
    answer.append(cnt)
    return answer

examples = [[[93, 30, 55], [1, 30, 5], [2, 1]], [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1], [1, 3, 2]]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42586/solution_groups?language=python3
def others():
    def other_42586(progresses, speeds):
        Q=[]
        for p, s in zip(progresses, speeds):
            if len(Q)==0 or Q[-1][0]<-((p-100)//s):
                Q.append([-((p-100)//s),1])
            else:
                Q[-1][1]+=1
        return [q[1] for q in Q]



