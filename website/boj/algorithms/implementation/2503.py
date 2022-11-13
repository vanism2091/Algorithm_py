
"""
세 자리 숫자 야구 게임
1~9까지 1~9: 9**3 = 729
각 대답마다 해당하는 것만 남기고 나머지는 지운다
경우의 수는 729 * 100 정도?
->
각각 경우의 친구들을 모두 구한 후, set intersection 한다

!!!! 서로 다른 숫자 3개.. :)
문제를 제발 잘 읽자 :)
"""
from itertools import permutations
# 숫자 야구
# https://www.acmicpc.net/problem/2503
def sol_2503():
    import sys
    inputs = sys.stdin.read().splitlines()
    cand = [f'{i}{j}{k}' for i,j,k in permutations(range(1,10),3)]

    def get_str_ball(str1, str2):
        num_strike = [ c1 == c2 for c1, c2 in zip(str1, str2)].count(True)
        num_ball = 0
        for c in str1:
            if c in str2:
                num_ball += 1
        return num_strike, num_ball - num_strike

    for i in range(1, int(inputs[0])+1):
        res = []
        guess, s, b = map(int, inputs[i].split())
        guess = str(guess)
        for n in cand:
            if get_str_ball(n, guess) == (s, b):
                res.append(n)
        cand = res
    print(cand)
    return len(cand)
        

if __name__ == "__main__":
    print(sol_2503())

"""
체크 함수 - 나는 O(3+3+a(zip등등))인데 이렇게 구현하면 O(3*3(in))이면 가능
이 아니라, string in 의 time complexity는 brute-force보다 더 적다고 한다.
https://stackoverflow.com/questions/18139660/python-string-in-operator-implementation-algorithm-and-time-complexity
https://stackoverflow.com/questions/68060511/time-complexity-with-strings-in-python
지금은 안읽히니 나중에 꼭 읽어보자... :)

굳이 string으로 변환할 필요 없이, 튜플도 인덱싱이 되니까 :)ㅇㅋㅇㅋ
근데 굳이 할당해서 비교문 and로 묶을 필요는 없는듯. :)
"""
# https://www.acmicpc.net/problem/status/2503/1003/1
def other_2503():
    import sys
    from itertools import permutations
    input = sys.stdin.readline
    n = int(input())
    s = list(permutations(range(1,10), 3))
    def check(num, tar):
        st = 0
        ball = 0
        for i in range(3):
            if str(num[i]) == tar[i]: st+=1
            elif str(num[i]) in tar: ball+=1
        return (st, ball)

    for i in range(n):
        arr = []
        tar, st, ball = map(int, input().split())
        for num in s:
            tst, tball = check(num, str(tar))
            if tst==st and tball == ball:
                arr.append(num)
        s = arr
    print(len(s))

