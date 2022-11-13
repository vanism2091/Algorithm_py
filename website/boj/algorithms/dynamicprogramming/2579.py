
"""
계단 오르기
점화식을 찾아보자
1. 계단은 한 번에 한 계단 혹은 두 계단 식 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안된다.
3. 마지막 도착 계단은 반드시 밟아야 한다.

1 - 1.
2 - 1 + 2
3rd - 1+2+3은 안됨.  max 1+3 / 2+3
4th - 2까지의 max + 4 / 1까지 max + 3+4 
nth - max(f(n-3)+s[n-1]+s[n] / f(n-2)+s[n] 
"""

# 계단 오르기
# https://www.acmicpc.net/problem/2579
def sol_2579():
    from sys import stdin
    N, *scores = map(int, stdin.readlines())
    d = [0] * (N+1)
    d[1] = scores[0]
    if len(scores) > 1: 
        d[2] = scores[0]+scores[1]
    if N >= 3:
        for i in range(3, N+1):
            d[i] = max(d[i-3]+scores[i-2]+scores[i-1], d[i-2]+scores[i-1])
    print(d[N])


# https://www.acmicpc.net/problem/status/2579/1003/1
def other_2579():
    pass



