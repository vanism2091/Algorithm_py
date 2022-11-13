
import os
from re import L
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
소수 리스트를 만든 후,
넘버에서 만들 수 있는 조합을 찾아서, 소수인지 아닌지 체크한다.
"""

# 1 2 3
# 12 21 13 31 23 32
# 123 231 321 132 213 312
from itertools import permutations
# 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
def solution(numbers):
    len_num = len(numbers)
    max_num = int(max(list(numbers)) * len_num)
    is_prime = [False, False, True] + [True] * (max_num-2)
    for i in range(2, int(max_num**.5)+1):
        if is_prime[i]:
            for j in range(i*2, max_num+1, i):
                is_prime[j] = False
    
    new_nums = set()
    for i in range(1, len_num+1):
        for p in permutations(range(len_num), i):
            new_num = ''
            for idx in p:
                new_num += numbers[idx]
            new_nums.add(int(new_num))

    return [is_prime[i] for i in new_nums].count(True)

examples = [['17', 3], ['011', 2]]

test_cases(solution, examples)

"""
에라토스테네스의 체?
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42839/solution_groups?language=python3
def others():
    from itertools import permutations
    def solution(n):
        a = set()
        for i in range(len(n)):
            a |= set(map(int, map("".join, permutations(list(n), i + 1))))
        a -= set(range(0, 2))
        for i in range(2, int(max(a) ** 0.5) + 1):
            a -= set(range(i * 2, max(a) + 1, i))
        return len(a)

def others_2():
    primeSet = set()

    def isPrime(number):
        if number in (0, 1):
            return False
        for i in range(2, number):
            if number % i == 0:
                return False

        return True


    def makeCombinations(str1, str2):
        if str1 != "":
            if isPrime(int(str1)):
                primeSet.add(int(str1))

        for i in range(len(str2)):
            makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


    def solution(numbers):
        makeCombinations("", numbers)

        answer = len(primeSet)

        return answer

"""
라이브러리 없이 품 ㄷ
"""
def others_3():
    # 0으로 시작하는 숫자. 
    # 모든 숫자의 조합.

    def isPrimeNumber(number):
        if number <= 1:
            return False
        else:
            for i in range(2, number // 2 + 1):
                if number % i == 0:
                    return False
            return True

    def getAllCombination(numbers, numList, leftCipher):
        '''
        numbers : 총 숫자카드 list
        numList : 가능한 숫자 배열 list
        leftCipher : 남은 자릿수
        '''

        # 현재 가능한 숫자 배열 list를 기준으로 추가가 가능한 숫자들은 찾는다. 
        newNumList = [[]]
        for li in numList:
            for i in numbers:
                if i in li and li.count(i) <= numbers.count(i) - 1:
                    tmp = li[:]
                    tmp.append(i)
                    newNumList.append(tmp)
                if i not in li:
                    tmp = li[:]
                    tmp.append(i)
                    newNumList.append(tmp)

        leftCipher -= 1

        if leftCipher == 0:
            return newNumList
        else:
            return getAllCombination(numbers, newNumList, leftCipher)

    def removeFirstZero(numList):
        for i, num in enumerate(numList):
            firstNumIsZero = bool()

            while True:
                if len(num) >= 2 and num[0] == '0':
                    firstNumIsZero = True
                else:
                    numList[i] = num
                    break

                num = num[1:]

    def getUnique2DList(numList):
        for i, val in enumerate(numList):
            tmp = str()
            for char in val:
                tmp += char
            numList[i] = tmp

        newList = list(set(numList))
        return newList

    def solution(numbers):    
        availableAnswer = getAllCombination(numbers, [[]], len(numbers))
        del availableAnswer[0]
        removeFirstZero(availableAnswer)
        availableAnswer = getUnique2DList(availableAnswer)

        answer = 0
        for val in availableAnswer:
            if isPrimeNumber(int(val)):
                print(val)
                answer += 1

        return answer

