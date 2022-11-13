"""
기존의 dp 문제 처럼,
제일 가벼운 친구를 시작으로, dp를 만들어가보자

1. 아이템은 1개만 갖고 갈 수 있다는 당연한 사실 :)
2. 20% 쯤에서 틀림 ㅜㅠ
3. 내 생각엔, 같은 무게 N개인 경우, 1개만 카운트돼서 그런듯 24에서 틀림 :)
"""
# 평범한 배낭
# https://www.acmicpc.net/problem/12865
# def sol_12865():
import sys
N, K = map(int, input().split())
items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
items = sorted(items, key=lambda x: -x[1])
items.sort()
min_weight = items[0][0]

if K < min_weight:
    print(0)

# DP table 초기화
d = [0] *(K+1)
got = [[] for _ in range(K+1)]

d[min_weight] = items[0][1]
got[min_weight].append(items[0])
for idx in range(min_weight+1, K+1):
    c, g = d[idx-1], got[idx-1]
    for w, v in items:
        if idx < w: break
        if (w, v) in got[idx-w] and c < d[idx-w]:
            c = d[idx-w]
            g = got[idx-w]
        else:
            c = d[idx-w] + v
            g = got[idx-w] + [(w, v)]
        
        if d[idx] < c:
            d[idx] = c
            got[idx] = g

print(d[K])
    # pass    


# https://www.acmicpc.net/problem/status/12865/1003/1
def other_12865():
    pass



# 6 13
# 3 8
# 3 6
# 5 12