
"""
이친숫
1. 0으로 시작하지 않음
2. 1이 두 번 연속 나타나지 않음

1자리 이친수 1
2자리 이친수 10
3자리   100, 101
4자리 1000 1001 1010
5자리 10000, 10001, 10010, 10100, 10101
피보나치네 :)

30840	80

어떤 분	29284	52
"""

# 이친수
# https://www.acmicpc.net/problem/2193
def sol_2193():
    n = int(input())
    d = [0, 1, 1]+[0]*88
    if n>=3:
        for i in range(3, n+1):
            d[i] = d[i-1]+ d[i-2]
    print(d[n])


# https://www.acmicpc.net/problem/status/2193/1003/1
def other_2193():
    pass



