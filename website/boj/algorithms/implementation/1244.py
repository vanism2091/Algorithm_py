
"""
N개의 스위치
1: 켜짐, 0: 꺼짐
학생 M명에게 [1,N] 수 1개씩 나눠줌.
학생들은 자신의 성별과 받은 수에 따라 스위치를 조작함
남학생: 자기가 받은 수의 배수의 스위치 상태를 바꿈
    e.g. 8개의 스위치. 3을 받았다 -> 3의 배수인 3, 6의 스위치 상태를 바꿈
여학생: 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 
    - 좌우가 대칭이면서 
    - 가장 많은 스위치를 포함하는 구간을 찾아서
    그 구간에 속한 스위치 상태를 모두 바꾼다.
    이때, 구간에 속한 스위치 개수는 항상 홀수가 된다.
input: 
    1. 스위치 개수 N [1, 100]
    2. 스위치 현재 상태
    3. 학생 수 M [1, 100]
    4~. 성별(1:남, 2:여) 받은 수 [1, N] 
output
    switch[:20]
    switch[20:40] ... 20개씩 출력, 빈칸으로 구분
비트 연산?
"""
# 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244
# def sol_1244():
import sys
inputs = sys.stdin.read().splitlines()
N = int(inputs[0])
switches = [0] + list(map(int,inputs[1].split()))
# for s in inputs[3:]: # 이거 했을때 계속 오류남 아...
for s in inputs[3:]:
# for i in range(int(inputs[2])):
    gender, num = map(int, s.split())
    # gender, num = map(int, inputs[3+i].split())
    if gender == 1:
        for i in range(1,N//num+1):
            switches[num * i] = 1 - switches[num * i]
    else:
        switches[num] = 1 - switches[num]
        l, r = num-1, num+1
        while l and r<=N and switches[l] == switches[r]:
            switches[l], switches[r] = 1 - switches[l], 1 - switches[r]
            l, r = l-1, r+1
switches = switches[1:]
for i in range((N-1)//20 + 1):
    for switch in switches[20*i:20*(i+1)]:
        print(switch, end=" ")
    print()

"""
25
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
1
1 1
"""


if __name__ == "__main__":
    print(sol_1244())

"""

"""
# https://www.acmicpc.net/problem/status/1244/1003/1
def other_1244():
    pass



