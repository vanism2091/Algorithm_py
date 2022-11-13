
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
0 또는 양의 정수가 주어졌을 때, 
정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내라.
len(numbers) : [1, 100_000]
numbers: [0, 1_000]
"""
# 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3
def solution(numbers):
    answer = ''
    def new_str(nstr):
        if len(nstr) == 1:
            return nstr * 3
        elif len(nstr) == 2:
            return nstr + f'{int(nstr[0]) + (-.5 if nstr[0] > nstr[1] else .5)}'
        elif nstr == '1000':
            return '1'
        else:
            return nstr
    numbers = map(str, numbers)
    numbers = sorted([(n, new_str(n)) for n in numbers], key=lambda x:x[1], reverse=True)
    print(numbers)
    answer = ''.join([n[0] for n in numbers])
    return answer

# examples = [[[0, 6, 10, 2, 1000], '621010000'], [[3, 30, 34, 5, 9,0], '95343300']]
examples = [[[98, 989, 1000], '989981000'], [[3, 30, 34, 5, 9,0], '95343300']]

"""
9 93

606 60 605
677 67 676 675
667 66 666 665
656 65 655

테스트 1 〉	통과 (73.46ms, 24.2MB)
테스트 2 〉	통과 (34.17ms, 17.8MB)
테스트 3 〉	통과 (91.39ms, 28.3MB)
테스트 4 〉	통과 (1.58ms, 10.8MB)
테스트 5 〉	통과 (57.35ms, 22.3MB)
테스트 6 〉	통과 (46.02ms, 20.9MB)
테스트 7 〉	통과 (0.05ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
    테스트 11 〉	실패 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.04ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)

:(
len2 일때 +- 0.5

테스트 케이스 11: 0,0,0,0 -> 0
"""
test_cases(solution, examples)

"""
내가 new_str 로 했던 구현을
sort key로 했음. * 3을 하면 편하구나 :)
344 -> 344344344
34 -> 343434
343 -> 343343343
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42746/solution_groups?language=python3
def others():
    def solution(numbers):
        numbers = list(map(str, numbers))
        numbers.sort(key=lambda x: x*3, reverse=True)
        return str(int(''.join(numbers)))



