
"""
돌게임
둘이서 하는 게임. 탁자 위에 돌 N개가 있음
번갈아서 돌을 가져가며 1개  또는 3개 가져갈 수 있음
마지막 돌을 가져가는 사람이 게임을 이기게 됨
완벽히 게임을 했을 때, 이기는 사람을 구하는 프로그램.
게임은 상근이가 먼저 시작함. "SK" "CY"

상근이는 0, 창영이는 1이라고 하자
시작은 상근이가. 상근이의 입장에서 게임을 보자.
1-0     2-1    3-0  4-1    5-0     6-1 ?????!!!!!
ㅋㅋ.. dp도 적용 해볼까 하하..
"""

# 돌 게임
# https://www.acmicpc.net/problem/9655
def sol_9655():
    n = int(input())
    print("SK" if n%2 else "CY")
    pass


# https://www.acmicpc.net/problem/status/9655/1003/1
def other_9655():
    pass


