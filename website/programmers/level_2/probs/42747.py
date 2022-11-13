
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
H-index: 과학자의 생산성과 영향력을 나타내는 지표
h를 구하고 싶다.
논문 n편 중 h번 이상 인용된 논문이 h편 이상이고,
나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 H-index
논문 인용 횟수를 담은 배열 -> H-index

constraint
논문의 수: [1, 1_000]
논문 별 인용 횟수 [0, 10_000]
e.g.
    [3, 0, 6, 1, 5]	    3
    [0, 1, 3, 5, 6]
    [6 5 3 1 0]
논문 5편 중, 3번 이상 인용된 논문이 3편 이상, 나머지 논문이 3번 이하 인용
"""
from bisect import bisect_left
# H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3
def solution(citations):
    answer = 0
    c_unq = sorted(list(set(citations)), reverse=True)
    c_len = len(citations)
    citations.sort()
    for n in c_unq:
        if c_len - bisect_left(citations, n) >= n:
            return n
    return answer


"""
테스트 1 〉	실패 (0.22ms, 10.2MB)
테스트 2 〉	실패 (0.36ms, 10.1MB)
테스트 3 〉	실패 (0.31ms, 10.2MB)
테스트 4 〉	실패 (0.29ms, 10MB)
테스트 5 〉	실패 (0.36ms, 10.2MB)
테스트 6 〉	실패 (0.37ms, 10MB)
테스트 7 〉	실패 (0.16ms, 10.4MB)
테스트 8 〉	실패 (0.03ms, 10.2MB)
테스트 9 〉	실패 (0.05ms, 10.1MB)
테스트 10 〉	실패 (0.21ms, 10.2MB)
테스트 11 〉	통과 (0.42ms, 10.2MB)
테스트 12 〉	실패 (0.07ms, 10.1MB)
테스트 13 〉	실패 (0.40ms, 10.4MB)
테스트 14 〉	실패 (0.36ms, 10.1MB)
테스트 15 〉	실패 (0.37ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)

문제 설명을 개떡같이했누... :):):)
2트가즈아
index로 해야함
"""
def solution(citations):
    answer = 0
    c_len = len(citations)
    citations.sort()
    for i in range(c_len+1,-1,-1):
        if c_len - bisect_left(citations, i) >= i:
            return i
    return answer


examples = [[[3, 0, 6, 1, 5], 3],[[0,0,0,0], 0],[[9,7,6,2,1],3]]

test_cases(solution, examples)

"""
citation 정렬 후,
enumerate(citations, start=1)
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42747/solution_groups?language=python3
def others():
    def solution(citations):
        citations.sort(reverse=True)
        answer = max(map(min, enumerate(citations, start=1)))
        return answer

    def solution(citations):
        citations = sorted(citations)
        l = len(citations)
        for i in range(l):
            if citations[i] >= l-i:
                return l-i
        return 0




