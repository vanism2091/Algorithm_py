
"""
# 브랜드별 패키지 가격, 개당 가격 list에서 min을 구함
# 패키지, 개별 = [(0, n), (1, n-6), ... (k, n-k*6) ],
#   단 k는 n <= 6*k인 k 중 최소
# tuple 순회하며 min_cost를 구한다
"""
# 기타줄
# https://www.acmicpc.net/problem/1049
def sol_1049():
    n, m = map(int, input().split())
    packs = []
    eachs = []
    for _ in range(m):
        a, b = map(int, input().split())
        packs.append(a)
        eachs.append(b)
    # O(M)
    # O(M) + O(M)
    p, e = min(packs), min(eachs)
    min_cost = 1000*100 + 1
    # O(logN)
    for i in range(n//6+2):
        curr_cost =  p*i + e* (n-i*6 if n-i*6 > 0 else 0)
        if min_cost > curr_cost:
            min_cost = curr_cost 
    return min_cost
    # O(M+logN)


if __name__ == "__main__":
    print(sol_1049())

"""
    # value에 다 넣고, 2칸씩 건너 뛰어서 slicing한 후 min을 구한다.. 
    # 오! 리스트가 1개라 공간 복잡도 측면에서 더 좋을듯.

    # 생각해보면 당연함. 개별로 6개 구매하는 것이 묶음 6개보다 더 싸면 전체 개별만 사면 됨
    # 이런 조건을 찾음으로써 평균 시간 복잡도 더 줄일 수 있음
    # 생각해보니.. 남은 경우는 두 가지밖에 없음
    #   1. 넘치는 한이 있어도 다 묶음으로 사거나
    #   2. 넘치기 전까지 묶음으로 + 개별로 사거나
    # 1, 2 중 min을 찾으면 됨
    # 문제를 읽고 더 생각하자 :)
"""
# https://www.acmicpc.net/problem/status/1049/1003/1
def other_1049():
    N,M=map(int,input().split())
    value=[]
    for i in range(M):
        value.extend(map(int,input().split()))
        a,b=min(value[::2]),min(value[1::2])

    if 6*b<a:
        print(b*N)
    else:
        print(min((N//6+1)*a,N//6*a+b*(N-N//6*6)))



