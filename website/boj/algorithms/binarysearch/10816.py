

"""
숫자 카드 2
상근이가 가진 N개의 숫자 카드
주어지는 M개의 정수 - 주어진 정수의 카드를 몇개 갖고 있는지 구하기
숫자 카드를 정렬 후에
bisect의 bisect_left, bisect_right 쓰면 될듯

[-1, 3, 2, 5], 10 인 경우 left_idx는 N이 나와서
cards[left_idx] 하면 IndexError가 나옴.
left_idx == N 조건문을 추가해야함. 
"""
   
# 숫자 카드 2
# https://www.acmicpc.net/problem/10816
# Python3 134772	1544
# PyPy3 224444	820
def sol_10816():
    from bisect import bisect_left, bisect_right
    from sys import stdin
    input = stdin.readline
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    numbers = list(map(int, input().split()))
    cards.sort()
    for i in range(len(numbers)):
        num = numbers[i]
        left_idx = bisect_left(cards, num)
        if left_idx == N or num != cards[left_idx]:
            numbers[i] = 0
            continue
        right_idx = bisect_right(cards, num)
        numbers[i] = right_idx - left_idx
    print(numbers)
    pass


# 이거 dictionary로 해볼까..?
# ㅋㅋㅋㅋㅋㅋ딕셔너리로 하니까 Python3이 PyPy3 1차 답안 속도를 이김
# Python3   142696	736
# PyPy3     253736	512
def sol_10816():
    from sys import stdin
    input = stdin.readline
    N = int(input())
    cards = list(map(int, input().split()))
    card_dict = {}
    for card in cards:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1

    _ = input()
    numbers = list(map(int, input().split()))

    res = []
    for number in numbers:
        if number in card_dict:
            res.append(card_dict[number])
        else:
            res.append(0)
    return " ".join(map(str, res))

if __name__ == "__main__":
    print(sol_10816())

"""
1. input 받는 코드
    - 문제에 필요한 A, B만 받아오기 위해
    - splitlines로 stdin 안에 줄단위로 list를 만듬
2. 딕셔너리 만들기
    - 빠름의 답은 역시 딕셔너리였다
3. 리스트 컴프리헨션
    - 코드 길이를 줄일 수 있다
"""
# 235840	448
# https://www.acmicpc.net/problem/status/10816/1003/1
def other_10816():
    import sys
    stdin = sys.stdin.read().splitlines()
    A = map(int,stdin[1].split())
    B = map(int,stdin[3].split())
    dic = {}
    for n in A:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    print(' '.join(str(dic[n]) if n in dic else '0' for n in B))



