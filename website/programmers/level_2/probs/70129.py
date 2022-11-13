
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (12.98ms, 11.5MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.10ms, 10.3MB)
테스트 7 〉	통과 (0.16ms, 10.5MB)
테스트 8 〉	통과 (0.09ms, 10.4MB)
테스트 9 〉	통과 (7.21ms, 11.1MB)
테스트 10 〉	통과 (12.17ms, 11.3MB)
테스트 11 〉	통과 (11.23ms, 11.5MB)

꼬리 재귀를 써보고 싶었다!
"""
# 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129?language=python3
def solution(s):
    return bin_conv(s, 0, 0)

def bin_conv(s: str, remove_cnt: int, i: int):
    num_list = list(map(int, s))
    sum_list = sum(num_list)
    curr_remove = len(num_list) - sum_list
    
    if sum_list == 1:
        return [i+1, remove_cnt + curr_remove]

    return bin_conv(format(sum_list, 'b'), remove_cnt + curr_remove, i+1)

examples = [['110010101001', [3, 8]], ['01110', [3, 3]], ['1111111', [4, 1]]]

test_cases(solution, examples)


"""
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.12ms, 10.4MB)
테스트 10 〉	통과 (0.59ms, 10.2MB)
테스트 11 〉	통과 (0.16ms, 10.2MB)

새로 바꾼 재귀 함수로 돌리니까 시간복잡도 완전 줄어듬
1. 스트링을 쪼개서 리스트 만듬
2. 그러면서 int로 하나하나 매핑
하는게 시간 복잡도가 꽤 나오나봄..
"""
def bin_conv2(s: str, removed_cnt: int, i: int):
    sum_ones = s.count('1')
    curr_removed = removed_cnt + len(s) - sum_ones
    if sum_ones == 1:
        return [i+1, curr_removed]
    return bin_conv2(format(sum_ones, 'b'), curr_removed, i+1)


"""
int list로 바꾸는 대신, 
s.count('1')을 함. 얘도 O(N)이고, list 새로 만드는 것도 O(N)인데, 새로 리스트를 만들면 공간 복잡도가 증가함.
따라서 굳이 list를 만들 필요 없이, s.count('1')로 sum check해도 될듯
이 부분을 적용시켜서 새롭게 재귀함수를 짜보자.

테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.11ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 9.99MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.18ms, 10.4MB)
테스트 10 〉	통과 (0.49ms, 10.4MB)
테스트 11 〉	통과 (0.16ms, 10.2MB)
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/70129/solution_groups?language=python3
def others():
    def solution(s):
        a, b = 0, 0
        while s != '1':
            a += 1
            num = s.count('1')
            b += len(s) - num
            s = bin(num)[2:]
        return [a, b]


