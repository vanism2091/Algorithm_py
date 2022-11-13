
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

현재 최대 값 = 
    현재 행의 최대값이 이전 최대값과 같은 열이라면, 
        max(이전 최대값+현재2nd값, 이전2nd값+현재최대값)
    현재 2nd값 = max(위 둘 중 min)
2nd best를 항상 갖고 있어야함..
    같은 열이 아니라면, 
        현재 최대값 = 이전 최대값 + 현재 최대값
        현재 2nd값 = 이전 최대값 + 현재 2nd값
        (값, 열)
"""
# 땅따먹기
# https://school.programmers.co.kr/learn/courses/30/lessons/12913?language=python3
def solution_2(land):
    answer = [[0, -1], [0, -1]]
    def get_best_second(li):
        if li[0] > li[1]:
            mx, secondmax = li[0], li[1]
            mi, si = 0, 1
        else:
            mx, secondmax = li[1], li[0]
            mi, si = 1, 0
        for i in range(2, len(li)):
            if li[i] > mx:
                secondmax, mx = mx, li[i]
                mi, si = i, mi
            elif li[i] > secondmax: # mx, smx 같은 경우도 포함
                secondmax, si = li[i], i
        return (mx, mi), (secondmax, si)
            
    for row in land:
        curr_best, curr_second = get_best_second(row)
        if answer[0][1] == curr_best[1]:
            bs = answer[0][0] + curr_second[0]
            sb = answer[1][0] + curr_best[0]
            if bs > sb:
                answer[0], answer[1] = [bs, curr_second[1]], [sb, curr_best[1]]
            else:
                answer[0], answer[1] = [sb, curr_best[1]], [bs, curr_second[1]]
        else:
            answer[0], answer[1] = [answer[0][0] + curr_best[0], curr_best[1]], [answer[1][0] + curr_second[0], curr_second[1]] 
    
    return max(answer[0][0], answer[1][0])


"""
딱 2개만 갖고 있는게 말이 안됨..최댓값 2개에 대해서 가능한 만큼 dfs 갈기자
슬슬 자는게 좋지않을까 ?
걍 저 랜드에 누적합을 할거임
"""

def solution(land):
    answer = [[0, -1], [0, -1]]
    def get_best_second(li):
        if li[0] > li[1]:
            mx, secondmax = li[0], li[1]
            mi, si = 0, 1
        else:
            mx, secondmax = li[1], li[0]
            mi, si = 1, 0
        for i in range(2, len(li)):
            if li[i] > mx:
                secondmax, mx = mx, li[i]
                mi, si = i, mi
            elif li[i] > secondmax: # mx, smx 같은 경우도 포함
                secondmax, si = li[i], i
        return [mx, mi], [secondmax, si]
            
    for i in range(len(land)):
        land[i] = [ s+(answer[0][0] if idx!=answer[0][1] else answer[1][0])  for idx, s in enumerate(land[i])]
        answer = get_best_second(land[i])
    
    return max(land[-1])

# examples = [[[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]], 16]]
examples = [[[[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]], 4+2+6+8]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12913/solution_groups?language=python3
def others():
    def solution(land):
        for i in range(1, len(land)):
            for j in range(len(land[0])):
                land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

        return max(land[-1])



