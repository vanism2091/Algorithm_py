
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
가격이 떨어지지 않은 기간 몇 초인지 return
가격 [1, 10_000]
len(가격) [2, 100_000]
"""
# 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3
from collections import deque
# 일단 반복문 2개로 풀어보죠
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         curr_p = prices[i]
#         for price in prices[i+1:]:
#             if curr_p > price:
#                 cnt += 1
#                 break
#             cnt += 1
#         answer.append(cnt)
#     return answer

"""
1차 시도
반복문 2개로 :)
요약: 정확성은 모두 통과했으나 효율성은 모두 실패

테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.1MB)
테스트 3 〉	통과 (0.93ms, 10.2MB)
테스트 4 〉	통과 (0.89ms, 10.1MB)
테스트 5 〉	통과 (1.20ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 9.92MB)
테스트 7 〉	통과 (0.40ms, 10.3MB)
테스트 8 〉	통과 (0.53ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (1.23ms, 10.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
채점 결과
정확성: 66.7
효율성: 0.0
합계: 66.7 / 100.0
"""

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.95ms, 10.2MB)
테스트 4 〉	통과 (0.52ms, 10.4MB)
테스트 5 〉	통과 (0.60ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.29ms, 10.3MB)
테스트 8 〉	통과 (0.36ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.61ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (76.76ms, 15.9MB)
테스트 2 〉	통과 (57.71ms, 16MB)
테스트 3 〉	통과 (155.55ms, 16.2MB)
테스트 4 〉	통과 (84.97ms, 16.3MB)
테스트 5 〉	통과 (52.60ms, 15.5MB)

풀었뜨아..
0. prices: Stack으로 보고, 하나씩 꺼내면서 right에 쌓는다.
1. p_min: 뒤에서부터 하나씩 꺼냈을 때, 현재까지 등장한 price 중 최소값
2. 현재 price가 p_min보다 크면, right에서 몇 초동안 가격이 안떨어졌는지 체크
3. 현재 price가 p_min보다 작거나 같으면, 구하려는 값은 res의 길이임
"""
def solution(prices):
    right = deque([prices.pop()])
    p_min = right[0]
    res = [0]
    
    while prices:
        curr_score = 0
        price = prices.pop()
        if price > p_min:
            # right를 보면서 res ++ 하기
            for i in range(len(right)):
                if price > right[i]:
                    curr_score = i + 1
                    break
            res.append(curr_score)
        elif price <= p_min:
            res.append(len(res))
            p_min = price
        right.appendleft(price)
    return res[::-1]


"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.39ms, 10.3MB)
테스트 4 〉	통과 (0.43ms, 10.3MB)
테스트 5 〉	통과 (0.31ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.16ms, 10.2MB)
테스트 8 〉	통과 (0.19ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.57ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (28.00ms, 18.7MB)
테스트 2 〉	통과 (19.45ms, 17.4MB)
테스트 3 〉	통과 (29.67ms, 19.9MB)
테스트 4 〉	통과 (24.14ms, 18.1MB)
테스트 5 〉	통과 (16.10ms, 17.3MB)

다른 사람 풀이를 참고해서 수정해본 코드
"""
def solution_after(prices):
    s = []
    answer = [0] * len(prices)
    for idx, price in enumerate(prices[:-1]):
        while s and s[-1][1] > price:
            p, _ = s.pop()
            answer[p] = idx - p
        s.append([idx, price])
    for idx, _ in s:
        answer[idx] = len(prices) - 1 - idx
    return answer

# prices = [1, 2, 2, 3, 4, 3, 5, 2, 3, 1, 4]
# [10, 8, 7, 4, 1, 2, 1, 2, 1, 1, 0]
examples = [[[1, 2, 3, 2, 3], [4, 3, 1, 1, 0]], [[1, 2, 2, 3, 4, 3, 5, 2, 3, 1, 4], [10, 8, 7, 4, 1, 2, 1, 2, 1, 1, 0]]]

test_cases(solution_after, examples)



"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42584/solution_groups?language=python3
def others():
    def solution(p):
        ans = [0] * len(p)
        stack = [0]
        for i in range(1, len(p)):
            if p[i] < p[stack[-1]]:
                for j in stack[::-1]:
                    if p[i] < p[j]:
                        ans[j] = i-j
                        stack.remove(j)
                    else:
                        break
            stack.append(i)
        for i in range(0, len(stack)-1):
            ans[stack[i]] = len(p) - stack[i] - 1
        return ans

    """
    ㅇㅎ..
    stack에 idx, price를 쌓으면서 진행하는데, 
    현재 price보다 더 큰 스택 내 price들은 꺼내서 answer index update함
    stack안에는 아직 answer 업뎃 안된 친구들만 남음.
    마지막에 얘네 꺼내서 업뎃해줌
    위는 아래랑 거의 비슷한데, 약간 다름
    """
    def solution(prices):
        stack = []
        answer = [0] * len(prices)
        for i in range(len(prices)):
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
            stack.append([i, prices[i]])
        for i, _ in stack:
            answer[i] = len(prices) - 1 - i
        return answer



