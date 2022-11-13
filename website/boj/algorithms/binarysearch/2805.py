## TODO: study!!!


"""
나무 자르기
이거 떡문제랑 똑같구나
파이썬으로 시간초과... ㄷ... ㄷ... 
그래서 PyPy3으로 하니까 맞음.. 526
근데 이걸 파이썬으로 맞힌 사람이 있네요? 나중에 확인해보자 ... ㄹㅎㅎㅎ
262760	524
"""

# 나무 자르기
# https://www.acmicpc.net/problem/2805
def sol_2805():
    _, M = map(int,input().split())
    trees = list(map(int, input().split()))

    start = 0
    end = max(trees)
    answer = 0
    while start <= end:
        mid = (start+end)// 2
        curr_sum = 0
        for i in trees:
            if mid < i:
                curr_sum += i-mid
        if curr_sum >= M:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)
    pass

# Python3  >    148408	1568
# 중간에 break 종료 조건을 하나 추가했는데, 시간초과는 벗어남
# PyPy3 262768	492
def sol_2805():
    _, M = map(int,input().split())
    trees = list(map(int, input().split()))

    start = 0
    end = max(trees)
    while start <= end:
        mid = (start+end)// 2
        curr_sum = 0
        for i in trees:
            if mid < i:
                curr_sum += i-mid
            if curr_sum >= M:
                break
        if curr_sum >= M:
            start = mid + 1
        else:
            end = mid - 1
    print(start - 1)

if __name__ == "__main__":
    sol_2805()


# input 받는 방식 바꾸기
# PyPy3     233092	392
def sol_2805():
    import sys
    input = sys.stdin.read().splitlines()
    _, M = map(int,input[0].split())
    trees = list(map(int, input[1].split()))

    start = 0
    end = max(trees)
    while start <= end:
        mid = (start+end)// 2
        curr_sum = 0
        for i in trees:
            if mid < i:
                curr_sum += i-mid
            if curr_sum >= M:
                break
        if curr_sum >= M:
            start = mid + 1
        else:
            end = mid - 1
    print(start - 1)


"""
woods -> Counter
1. start, end 합리적 정의
    start: (전체 나무 길이 - 필요한 나무 길이) // 나무 갯수
    end: 제일 긴 나무 길이 - 1
2. Counter를 이용해서 N을 C로 줄임
3. 이전 처럼, answer을 굳이 정의할 필요 없이 s + 1로 해도 될듯

start end를 합리적으로 잘 정의하는 것 + bs 회당 탐색 횟수를 N에서 C로 줄인 것
"""
# https://www.acmicpc.net/problem/status/2805/1003/1
# Python 120684	408
def other_2805_1():
    import sys
    from collections import Counter


    def sol2805():
        n, m = map(int, sys.stdin.readline().split())
        woods = Counter(map(int, sys.stdin.read().split())).items()
        s, e = (sum([wood * c for wood, c in woods]) - m) // n, max(woods)[0]-1
        answer = 0
        while s <= e:
            mid = (s + e) // 2
            if sum([(wood - mid) * c if wood > mid else 0 for wood, c in woods]) >= m:
                answer = mid
                s = mid + 1
            else:
                e = mid - 1
        print(answer)
    

    if __name__ == '__main__':
        sol2805()


"""
1. start, end는 나와 같음
2. get: 높이가 n일 때, trees에서 구할 수 있는 나무의 총 길이
3. get이 M보다 크면, == 원하는 나무 M 보다 n일때 얻을 수 있는 나무의 길이가 길다
    best가 get_-M(얻은 나무-얻고싶은 나무 차이) 보다 크다면,
    best = get_ - M, best_i = now
로직으로는 큰 차이가 없어보이는데.. input의 문제인가? 
input 바꾸니 내 코드도 PyPy3 기준 392가 됨
"""
# PyPy3	196564	376
def other_2805_2():
    import sys

    input_ = sys.stdin.read().splitlines()
    N,M = map(int,input_[0].split())
    trees = [ int(i) for i in input_[1].split()]

    max_ = max(trees)
    min_ = 0
    now = (max_+min_)//2
    best = 99999999999
    best_i = max_

    def get(trees, n):
        count = 0
        for i in trees:
            if(i - n >0):
                count += (i-n)
        return count

    while(max_ >= min_):
        get_ = get(trees,now)
        if(get_ >= M):
            if(best > get_ - M):
                best = get_ - M
                best_i = now
            min_ = now+1
        else:
            max_ = now-1
        now = (max_ + min_)//2

    print(best_i)
    pass



