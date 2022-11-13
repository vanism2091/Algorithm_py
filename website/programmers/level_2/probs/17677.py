
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

"카카오 신입 개발자 공채" 검색 시
- 카카오 첫 공채..'블라인드' 방식 채용
- 카카오, 합병 후 첫 공채.. 블라인드 전형으로 개발자 채용
- 카카오, 블라인드 전형으로 신입 개발자 공채
- 카카오 공채, 신입 개발자 코딩 능력만 본다
- 카카오, 신입 공채.. "코딩 실력만 본다"
- 카카오 "코딩 능력만으로 2018 신입 개발자 뽑는다"
기사의 제목을 기준으로 "블라인드 전형"에 주목하는 기사와 "코딩 테스트"에 주목하는 기사로 나뉨.

융사한 기사를 묶는 기준: 자카드 유사도
집합 A, B
J(A, B) =  len(A & B) / len(A + B)
A, B가 모두 공집합이면 J(A, B) 1

중복 허용하는 다중 집합에 확장. 
A = {1, 1, 2, 2, 3}
B = {1, 2, 2, 4, 5}
A&B = {1, 2, 2}
A+B = {1, 1, 2, 2, 3, 4, 5} 1: 두 집합 중 max count
J(A, B) = 3/7, 약 0.42

문자열 유사도 계산
"FRANCE"와 "FRENCH"
A: {FR, RA, AN, NC, CE}, 
B: {FR, RE, EN, NC, CH}
교집합은 {FR, NC}, 
합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}
J("FRANCE", "FRENCH") = 2/8 = 0.25

입력: 
    - st1, st2. len(str): [2, 1_000]
    - 각 문자열은 두 글자씩 끊어서 다중 집합의 원소로 만든다. 이때, 
    - 영문자 쌍 외의 글자가 있다면 그 쌍은 버린다. > isalpha()
    - 대소문자 차이는 무시한다. > lower()
"""
# [1차] 뉴스 클러스터링
# https://school.programmers.co.kr/learn/courses/30/lessons/17677?language=python3
def solution(str1, str2):
    K = 65536
    # 다중 집합
    s1_ms = [ str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2_ms = [ str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1_ms and not s2_ms:
        return K
    # 다중집합 합집합 원소 개수 구하기
    def get_res(s1, s2):
        if len(s1) > len(s2):
            # temp, res, target = s1.copy(), s1.copy(), s2
            res = get_intersection_num(s1,s2) / get_union_num(s1, s2)
        else: 
            res = get_intersection_num(s2,s1) / get_union_num(s2, s1)
        return int(K*res)
    
    def get_union_num(s1, s2):
        temp = s1.copy()
        cnt = len(s1)
        for e in s2:
            if e not in temp:
                cnt += 1
            else:
                temp.remove(e)
        return cnt

    def get_intersection_num(s1, s2):
        temp = s1.copy()
        cnt = 0
        for e in s2:
            if e in temp:
                cnt += 1
                temp.remove(e)
        return cnt

    return get_res(s1_ms, s2_ms)

examples = [['FRANCE', 'french', 16384], ['handshake', 'shake hands', 65536], ['aa1+aa2', 'AAAA12', 43690], ['E=M*C^2', 'e=m*c^2', 65536]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/17677/solution_groups?language=python3
def others():
    import re
    import math

    def solution(str1, str2):
        str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
        str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

        gyo = set(str1) & set(str2)
        hap = set(str1) | set(str2)

        if len(hap) == 0 :
            return 65536

        gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
        hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

        return math.floor((gyo_sum/hap_sum)*65536)




"""
다중집합의 합집합
b: 1
    a_temp = [1, 2, 2, 3, 4, 5] ->  [2, 2, 3, 4, 5]
    a_result = [1, 2, 2, 3, 4, 5]
b: 1
    a_temp = [2, 2, 3, 4, 5]
    a_result = [1, 2, 2, 3, 4, 5] -> [1, 1, 2, 2, 3, 4, 5]
b: 2
    a_temp = [2, 2, 3, 4, 5] -> [2, 3, 4, 5]
    a_result = [1, 1, 2, 2, 3, 4, 5]
b: 3
    a_temp = [2, 3, 4, 5] -> [2, 4, 5]
    a_result = [1, 1, 2, 2, 3, 4, 5]
b: 4
    a_temp = [2, 4, 5] -> [2, 5]
    a_result = [1, 1, 2, 2, 3, 4, 5]
b: 6
    a_temp = [2, 5]
    a_result = [1, 1, 2, 2, 3, 4, 5, 6]

# 결과:
a_result

nested list가 아니므로 얕은 복사로도 ㄱㅊ
# a = [1,2,2,3,4,5]
# b = [1,1,2,3,4,6]

# a_temp = a.copy()
# a_result = a.copy()

# for i in b:
#     if i not in a_temp:
#         a_result.append(i)
#     else:
#         a_temp.remove(i)

# # 결과
# a_result

a_temp = a.copy()
result = []
for i in b:
    if i in a_temp:
        a_temp.remove(i)
        result.append(i)
"""
