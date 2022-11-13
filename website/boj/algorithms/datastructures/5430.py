
"""
deque를 쓰면 될 것 같음
"""
# AC
# https://www.acmicpc.net/problem/5430
from collections import deque

def sol_5430():
    from sys import stdin
    inputs = stdin.read().splitlines()
    res = ""
    for i in range(int(inputs[0])):
        funcs, n, li = inputs[1+(3*i):3+(3*i)+1]
        if li == "[]":
            li = deque([])
        else:
            li = deque(map(int,li[1:len(li)-1].split(",")))

        if funcs.count("D") > int(n):
            res += "error\n"
            continue
        
        reverse = False
        for f in funcs:
            if f == "R":
                reverse = not reverse
            else:
                if reverse:
                    li.pop()
                else:
                    li.popleft()
        if reverse:
            li.reverse()
        res += "["+",".join(map(str,li))+"]\n"
    return res

if __name__ == "__main__":
    print(sol_5430())

"""
1. 'RR' 는 안뒤집는 것과 동일하므로 ''로 바꿔준다
2. 왜 p - input에서 -1을 하는거지?
"""
# https://www.acmicpc.net/problem/status/5430/1003/1
def other_5430():
    from sys import stdin

    input = stdin.readline

    def solve():
        for _ in range(int(input())):
            # 'RR' 는 안뒤집는 것과 동일하므로 ''로 바꿔준다
            p = [*map(len, input()[:-1].replace('RR', '').split('R'))]

            n = int(input())
            arr = input()[1:-2].split(',')
            # [left, right) 가 출력된다
            left, right = sum(p[::2]), n - sum(p[1::2])

            if left <= right:
                # len(p) % 2 == 1 인 경우 왼쪽에서 오른쪽 방향
                arr = arr[left:right] if len(p) % 2 else reversed(arr[left:right])
                print(f"[{','.join(arr)}]")
            else:
                print('error')


    if __name__ == '__main__':
        solve()
        pass



