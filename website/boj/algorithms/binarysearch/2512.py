## TODO: study

"""
예산 
- 정해진 총액 내에서 가능한 한 최대의 총 예산 배정하기
    - 1. 모든 요청이 배정될 수 있는 경우, 요청한 금액을 그대로 배정
    - 2. 모든 요청이 배정될 수 없는 경우, 특정한 정수 상한액을 계산하여
            그 이상인 예산요청에는 모두 상한액을 배정.
            상한액 이하의 예산 요청에 대해서는 요청한 금액을 그대로 배정
- e.g. 국가 예산 485, 지방 예산 요청 120, 110, 140, 150
        상한액 127, 120, 110, 127, 127 -> 484로 최대
- start: 1, end: max(예산요청액) mid: 상한액
- curr_sum = sum([mid에 대해서 mid보다 작은건 그대로, 큰건 mid])
- if curr_sum > 전체 예산: X end = mid - 1
- if curr_sum <= 예산: O(저장), start = mid + 1
"""

# 	30840	100
#  다른  분은 50까지도  감.. 분석 한 번 할 필요가 있음
# 예산
# https://www.acmicpc.net/problem/2512
def sol_2512():
    from sys import stdin
    input = stdin.readline
    _ = int(input())
    budgets = list(map(int, input().split()))
    total_budget = int(input())
    start, end = 1, max(budgets)
    while start <= end:
        mid = (start+end)//2
        curr = 0
        for i in budgets:
            curr += i if i < mid else mid
        if curr >  total_budget:
            end = mid - 1
        else:
            answer = mid
            start  = mid + 1
    print(answer)
    pass


if __name__ == '__main__':
    sol_2512()
    # print(sol_1920())


# 다시 풀어보기
# 합리적인 start, end 를 생각해보자
# N: 지방의 수 [3, 10_000]
# 요청: [1, 100_000]
# 총 예산: [N, 1_000_000_000]
# 이것도 카운터를 써볼까? 아까 그 분 풀이처럼?

# input 방식 바꾸기
# start 0 -> N X N 이 아님
# Counter 사용
# 오히려 시간이 늘어남???
# Python3   32412	108
def sol_2512():
    from sys import stdin
    from collections import Counter

    input = stdin.read().splitlines()
    N = int(input[0])
    budgets = Counter(map(int, input[1].split())).items()
    total_budget = int(input[2])

    start, end = N, max(budgets[0])
    while start <= end:
        mid = (start+end)//2
        curr = 0
        for b, c in budgets:
            curr += b*c if b < mid else mid*c
            if curr > total_budget:
                break
        if curr >  total_budget:
            end = mid - 1
        else:
            start  = mid + 1
    return start-1

if __name__ == '__main__':
    sol_2512()



"""
1. input: sys.stdin.readline
2. get Max Allocation
    list를 우선 sorted함
    - i = [0...N-1] N 번동안 반복함
        budget: 가능한 예산의 총 합
        avg = budget // n
        - 만약 sorted의 i번째 값이 avg보다 크면: 
            return avg
        - 그렇지 않으면,
            budget -= current_request
            n -= 1
    - 루프 돌 동안 return이 안되었다 == request중 max값 리턴
    오.. 신박하다
"""
# https://www.acmicpc.net/problem/status/2512/1003/1
def other_2512():
    import sys


    def getMaxAllocation(requests, N, budget):
        sortedRequests = sorted(requests)
        n = N
        for i in range(N):
            avg = budget // n
            if sortedRequests[i] > avg:
                return avg
            budget -= sortedRequests[i]
            n -= 1
        return sortedRequests[N-1]


    if __name__ == '__main__':
        N = int(sys.stdin.readline())
        requests = list(map(int, sys.stdin.readline().split()))
        budget = int(sys.stdin.readline())
        print(getMaxAllocation(requests, N, budget))


"""
1. budgets을 sort한다
2. 위 풀이와 로직이 같다. 코드가 더 간결하게 구현되어 있을 뿐
"""
def other_2512_2():
    n = int(input())
    budgets = [int(_) for _ in input().split()]
    m = int(input())
    i = 0
    budgets.sort()
    for b in budgets:
        div = m//n
        if b < div:
            m -= b
            n -= 1
        else:
            print(div)
            break
    else:
        print(budgets[-1])
