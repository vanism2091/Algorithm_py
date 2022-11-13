
"""

"""
# 보물
# https://www.acmicpc.net/problem/1026
def sol_1026():
    # 어차피 출력은 B 정렬과 무관하므로 a, b를 정렬 작은수X큰수
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return sum([ i*j for i in a.sort() for j in b.sort(reverse=True)])

    # B를 바꾸지 않고 답을 구하는 방법을 생각/구현해보자


if __name__ == "__main__":
    print(sol_1026())

"""

"""
# https://www.acmicpc.net/problem/status/1026/1003/1
def other_1026():
    pass



