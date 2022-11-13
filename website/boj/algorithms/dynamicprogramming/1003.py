"""
피보나치 함수
N이 주어졌을 때, fibonacci(N)을 호출했을 때, 
0, 1이 각각 몇 번 출력되는지 구하는 프로그램
N=3일 때, 
f(3) -> f(2) + f(1)

f(2) -> f(1) + f(0)
f(1) -> f(1)
f(0) -> f(0)
+
f(1) -> f(1)
f(1)은 2번, f(0)은 한 번

0: (1, 0), 1: (0, 1) 2: (1, 1) 3:(1, 2), 4:(2, 3)...

cases를 map으로 했을 때는 틀렸고
list로 한 번 더 감쌌을 때는 맞았다. 
둘이 무슨 차이..?

30840	68

타인
29284	52
"""

# 피보나치 함수
# https://www.acmicpc.net/problem/1003
def sol_1003():
    from sys import stdin
    d = [(1,0), (0,1), (1,1)] + [None]*38
    cases = list(map(int,stdin.readlines().split()))[1:]
    N = max(cases)
    def elmtwise_add(t1, t2): return tuple(x+y for x, y in zip(t1, t2))
    if N >= 3:
        for i in range(3, N+1):
            d[i] = elmtwise_add(d[i-1], d[i-2])
    for case in cases:
        print(" ".join(map(str, d[case])))

    pass


# https://www.acmicpc.net/problem/status/1003/1003/1
def other_1003():
    pass



