
"""

"""
# 3의 배수
# https://www.acmicpc.net/problem/1769
def sol_1769():
    from collections import Counter
    n = int(input())
    count = 0
    def get_y(num):
        res = 0
        num_str = str(num).replace("0", "")
        for num, cnt in Counter(num_str).items():
            res += int(num) * cnt
            print(num, cnt, res)
        return res
    while n >= 10:
        count += 1
        n = get_y(n)
        print(n)
    print(count)
    print("YES" if n in (3, 6, 9) else "NO")



if __name__ == "__main__":
    print(sol_1769())

"""

"""
# https://www.acmicpc.net/problem/status/1769/1003/1
def other_1769():
    n=0
    a=input()
    while len(a)!=1:
        n+=1
        b=sum(list(map(int,list(a))))
        a=str(b)
    print(n)
    if int(a)%3==0:
        print("YES")
    else:
        print("NO")

n = input()

#
cnt = 0
def solution(arr):
    sum_num = 0
    global cnt
    for i in arr:
        sum_num += int(i)
    cnt += 1
    if len(str(sum_num)) == 1:
        if sum_num % 3 == 0:
            print(cnt)
            print('YES')
        else:
            print(cnt)
            print('NO')
    else:
        solution(str(sum_num))
if len(n) == 1:
    print(cnt)
    print('YES' if int(n) % 3 == 0 else 'NO')
else:
    solution(n)


