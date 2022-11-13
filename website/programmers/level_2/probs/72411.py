
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
단품 메뉴 -> 코스 메뉴로 재구성해 새로운 메뉴 제공
- 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
- 코스는 최소 2가지 이상의 단품 메뉴로 구성.
- 최소 2명 이상의 손님으로부터 주문된 단품 메뉴 조합에 대해서만 코스요리 후보

- 제한사항
- order 배열 크기 [2, 20]  2**20 : 1_000_000 백만 :)
"""
# 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411?language=python3
from collections import Counter
from itertools import combinations
def solution(orders, course):
    course_dict = {n: Counter() for n in course}
    # c = Counter()
    for order in orders:
        for i in course:
            course_dict[i].update(combinations(sorted(list(order)), i))
    answer = []
    for i in course:
        if len(course_dict[i]):
            curr_max = max(course_dict[i].values())
            answer.extend(["".join(i) for i, cnt in course_dict[i].items() if cnt > 1 and cnt == curr_max])
    return sorted(answer)

examples = [[['XYZ', 'XWY', 'WXA'], [2, 3, 4], ['WX', 'XY']]]
# examples = [[['ABCFG', 'AC', 'CDE', 'ACDE', 'BCFG', 'ACDEH'], [2, 3, 4], ['AC', 'ACDE', 'BCFG', 'CDE']], [['ABCDE', 'AB', 'CD', 'ADE', 'XYZ', 'XYZ', 'ACD'], [2, 3, 5], ['ACD', 'AD', 'ADE', 'CD', 'XYZ']], [['XYZ', 'XWY', 'WXA'], [2, 3, 4], ['WX', 'XY']]]

test_cases(solution, examples)

"""
- defaultdict 확인해보기
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/72411/solution_groups?language=python3
def others():
    import collections
    import itertools

    def solution(orders, course):
        result = []

        for course_size in course:
            order_combinations = []
            for order in orders:
                order_combinations += itertools.combinations(sorted(order), course_size)

            most_ordered = collections.Counter(order_combinations).most_common()
            result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

        return [ ''.join(v) for v in sorted(result) ]

    from collections import defaultdict
    from itertools import combinations

    def solution(orders, course):
        d, m = defaultdict(int), defaultdict(lambda: 2)
        for order in orders:
            for n in [n for n in course if n <= len(order)]:
                for v in combinations(sorted(order), n):
                    d[v], m[n] = d[v] + 1, d[v] + 1 if d[v] >= m[n] else m[n]
        return sorted(["".join(v) for v, c in d.items() if c == m[len(v)]])



