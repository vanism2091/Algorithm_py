
"""
파도반 수열

점화식 꿰뚫어버렸따
f(n) = f(n-2) + f(n-3)
input 1~100

30840	68

다른사람    29284	52
"""

# 파도반 수열
# https://www.acmicpc.net/problem/9461
def sol_9461():
    from sys import stdin
    N, *cases = map(int, stdin.readlines())
    max_case = max(*cases, 4)
    d = [0, 1, 1, 1] + [0]*97
    for i in range(4, max_case+1):
        d[i] = d[i-2]+d[i-3]
    for case in cases:
        print(d[case])


# https://www.acmicpc.net/problem/status/9461/1003/1
def other_9461():
    pass



