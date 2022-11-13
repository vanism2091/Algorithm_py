
"""
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

역 연산
- 2로 나눈다
- 맨 뒤에 1을 뺀다.
전자보다 후자가 항상 숫자를 더 작게 만든다.
둘 모두 할 수 있는 경우는 존재하지 않는다.
"""
# A → B
# https://www.acmicpc.net/problem/16953
def sol_16953(a, b):
    # from sys import stdin
    # a, b = map(int, stdin.readline().split())
    res = 1
    while a < b:
        if b % 10 == 1:
            b //= 10
            res += 1
        elif b % 2 == 0:
            b //= 2
            res += 1
        else:
            break
    return res if a == b else -1
        
if __name__ == "__main__":
    # print(sol_16953())
    print(sol_16953(2, 162))
    print(sol_16953(4, 42))
    print(sol_16953(100, 40021))
"""

"""



"""
내 풀이랑 크게 다른 점을 못느끼겠는데 
"""
# https://www.acmicpc.net/problem/status/16953/1003/1
def other_16953():
    n,m = map(int,input().split())
    count=0
    while n!=m:
        if n>m:
            count=-2
            break
        elif str(m)[-1]=='1':
            m=m//10
            count+=1
        elif m%2==0:
            m=m//2
            count+=1
        else:
            count=-2
            break
    print(count+1)



