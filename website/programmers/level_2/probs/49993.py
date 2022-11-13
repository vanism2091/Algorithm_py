
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.04ms, 9.94MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)

시간복잡도 분석해보기
스킬: N,
타겟 총 길이: M
타겟 각자 길이: M_i
스킬 트리 갯수: T
"""
# 스킬트리
# https://school.programmers.co.kr/learn/courses/30/lessons/49993?language=python3
def solution(skill, skill_trees):
    answer = 0
    # O(T* (2N+M_i) ) = O(2N*T + M)
    for t in skill_trees:
        # O(2N+M_i)
        if is_possible_skill(skill, t):
            answer += 1
    return answer

def is_possible_skill(skill, target) -> bool:
    # O(N)
    s_dict = {char: 26 for char in skill}
    #(O(M_i))
    for i, c in enumerate(target):
        if c in skill:
            s_dict[c] = i
    temp = 0
    # O(N)
    for c in skill:
        if temp <= s_dict[c]:
            temp = s_dict[c]
        else:
            return False
    return True

examples = [['CBD', ['BACDE', 'CBADF', 'AECB', 'BDA'], 2]]

test_cases(solution, examples)

"""
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 9.99MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 9.92MB)
테스트 8 〉	통과 (0.01ms, 10MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)

시간복잡도 분석해보기
스킬: N,
타겟 총 길이: M
타겟 각자 길이: M_i
스킬 트리 갯수: T

python for-else 문:
break로 끊기지 않고 끝까지 수행되었을 때 else문 이하 실행함
"""
from collections import deque
def solution_after(skill, skill_trees):
    answer = 0

    # O(T * - ) = O(NT + M)
    for skills in skill_trees:
        # O(N)
        skill_list = deque(skill)
        
        # O(M_i)
        for s in skills:
            if s in skill:
                if s != skill_list.popleft():
                    break
        else:
            answer += 1

    return answer


"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/49993/solution_groups?language=python3
def others():
    def solution(skill,skill_tree):
        answer=0
        for i in skill_tree:
            skillist=''
            for z in i:
                if z in skill:
                    skillist+=z
            if skillist==skill[0:len(skillist)]:
                answer+=1
        return answer

    def solution(skill, skill_trees):
        return len(list(filter(lambda st:skill.find(''.join([s for s in list(st) if s in skill]))==0, skill_trees)))

    def solution(skill, skill_trees):
        answer = 0

        for skills in skill_trees:
            skill_list = list(skill)

            for s in skills:
                if s in skill:
                    if s != skill_list.pop(0):
                        break
            else:
                answer += 1

        return answer
    pass



