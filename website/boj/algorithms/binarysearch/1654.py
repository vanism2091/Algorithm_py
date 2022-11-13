## TODO: study

"""
랜선 자르기
오.. 이건 좀 다르다
K개의 다른 길이의 랜선으로 N개의 같은 길이의 랜선을 만들고 싶음
이때 만들 수 있는 최대 랜선 길이는?
start: 0, end: max(wires), mid: (start+end)//2
mid 길이를 각 N을 나눈 값.. 의 합..이 N보다 크거나 같으면, 기록 후 start를 mid+1
그렇지 않으면 end = mid-1

start를 1부터 해야 함.. 그렇지 않으면 나중에 modula zero divisor 에러남
// 30840	96
// 실행 시간 최소인 다른 분은  84임
"""
# 랜선 자르기
# https://www.acmicpc.net/problem/1654
def sol_1654():
    import sys
    N, M = map(int,input().split())
    wires = list(map(int, sys.stdin.readlines()))
    start, end = 1, max(wires)
    answer = 0
    while start <= end:
        mid = (start+end)//2
        curr = sum([w//mid for w in wires])
        if curr >= M:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)
    pass


"""
start: 1
end: sum(li) // N : 갖고 있는 랜선 길이 총합 // 필요한 랜선 갯수 (avg)
end를 더 합리적으로 잘 설정해서 속도가 조금 줄어든 듯
"""
# https://www.acmicpc.net/problem/status/1654/1003/1
def other_1654():
    from sys import stdin
    K, N = map(int,stdin.readline().split())
    li = list(map(int,stdin.readlines()))
    h, l = sum(li)//N, 1
    while l <= h :
        mid = (h+l)//2
        cnt = sum([x//mid for x in li])
        if cnt < N:
            h = mid - 1
        elif cnt >= N:
            l = mid + 1
            ans = mid
    print(ans)