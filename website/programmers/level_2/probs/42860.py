
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
조이스틱으로 알파벳 이름 완성하기. 맨 처음에는 A로만 이루어져 있다.

조이스틱 방향키 별 기능
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)

JAZ를 만들고 싶다:
- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.

커서는 처음부터 시작. A에서 min(위로 J, 아래로 J)
min을 어떻게 구하면 좋을까?
ord('A') = 65, ord('Z') = 90 
* = ord('Z') - ord('A') = 25
min(26-*, *)

이거 커서가 자동으로 움직이는게 아니구낭..
일단 위아래 리스트를 만든 후에, 
len(name) - 1 후, A가 두번째에 있거나 끝에 있다면 -1을 또 한다.
"""
# 조이스틱
# https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3

def solution_1(name):
    num_A = ord('A')
    if len(name) == 1:
        return min(26-(ord(name)-num_A), (ord(name)-num_A)) 
    min_ud = [min(26-(ord(c)-num_A), (ord(c)-num_A)) for c in name]
    return sum(min_ud) + len(name) + (-2 if name[1] == 'A' or name[-1] == 'A' else -1)
# 생각해보면, JAAAAA 도 있음 ㅎㅎ

"""
1차시도 후 10번부터 실패(17개) 및 런타임 에러(1개) -> 일단 str 1일때 케이스를 추가했음.
런타임 에러만 1개 사라질듯
1. A의 갯수를 센다 (0)
2. > 방향일 때, 처음부터 A를 체크한다. 남아있는 원소의 수 == A의 수일때 break.
3. < 방향일 때, ...

정확성: 59.3
합계: 59.3 / 100.0
"""

def solution_2(name):
    num_A = ord('A')
    if len(name) == 1:
        return min(26-(ord(name)-num_A), (ord(name)-num_A)) 
    min_ud = [min(26-(ord(c)-num_A), (ord(c)-num_A)) for c in name]
    
    def get_move(arr):
        # [1:] 을 넣을 예정.
        num_zero = arr.count(0)
        if num_zero == 0 or arr[-1] != 0:
            return len(arr)
        remainders = len(arr)
        for i, n in enumerate(arr, start=1):
            if remainders == num_zero:
                return i - 1
            if n == 0: 
                num_zero -= 1
            remainders -= 1
    min_lr = min(get_move(list(reversed(min_ud[1:]))), get_move(min_ud[1:]))
    return sum(min_ud) + min_lr

"""
단방향이어선 안됨
BBAAAAAB 의 경우, > < < 이 제일 짧음..:)
AAA가 제일 길게 연속되는 부분의 첫, 마지막 index를 구해야함.

BBBAAAAAAAABB : 6 > > < < | < < 

BBBBAABBBB

정확성: 70.4
합계: 70.4 / 100.0


다시 고침.
ABAAABB , ABBAAAB 둘은 > < 어디로 먼저갔는지에 따라 달라진다..
정확성: 96.3
합계: 96.3 / 100.0

이거 고치고 나니까 17번 런타임 에러만 남음 - A만 있을 때 == 0
if 문 추가했고, 해결은 했는데 너무 더러워보인다.....:)

정리 후에 다른 분 풀이를 보자... :)
"""

def solution(name):
    num_A = ord('A')
    if len(name) == 1:
        return min(26-(ord(name)-num_A), (ord(name)-num_A))
    if len(name) == name.count('A'):
        return 0
    min_ud = [min(26-(ord(c)-num_A), (ord(c)-num_A)) for c in name]
    if min_ud.count(0):
        z_idx = []
        z_l, z_r = 0, 0
        new_zero = True
        for i, n in enumerate(min_ud):
            if n == 0:
                if new_zero:
                    z_l = i
                    new_zero = False
                z_r = i
            if n != 0:
                if not new_zero:
                    z_idx.append((z_l, z_r))
                    new_zero = True
        
        num_c_z = [j-i for i, j in z_idx]
        a, b = z_idx[num_c_z.index(max(num_c_z))]
        #  lr_move = (a-1) * 2 + len(name) - b - 1
        if a-1 > len(name)-b-1:
            M, m = a-1, len(name)-b-1
        else:
            m, M = a-1, len(name)-b-1
        lr_move = m * 2 + M
        
        def get_move(arr):
            # [1:] 을 넣을 예정.
            num_zero = arr.count(0)
            if arr[-1] != 0:
                return len(arr)
            remainders = len(arr)
            for i, n in enumerate(arr, start=1):
                if remainders == num_zero:
                    return i - 1
                if n == 0: 
                    num_zero -= 1
                remainders -= 1
        min_lr = min(get_move(list(reversed(min_ud[1:]))), get_move(min_ud[1:]), lr_move)
    else:
        min_lr = len(name)-1
    return sum(min_ud) + min_lr

examples = [ ['AAAAAAAAA', 0]]
# examples = [['JEROEN', 56], ['JAN', 23], ['JANAAAAA', 24]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42860/solution_groups?language=python3
def others():
    def solution(name):
        answer = 0
        n = len(name)

        def alphabet_to_num(char):
            num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
            return num_char[ord(char) - ord('A')]

        for ch in name:
            answer += alphabet_to_num(ch)

        move = n - 1
        for idx in range(n):
            next_idx = idx + 1
            while (next_idx < n) and (name[next_idx] == 'A'):
                next_idx += 1
            distance = min(idx, n - next_idx)
            move = min(move, idx + n - next_idx + distance)

        answer += move
        return answer



