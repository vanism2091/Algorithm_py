from typing import *
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

"""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # sol_1-book: 모든 조합 탐색
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값 자리수 단위 반복
            for i in range(index, len(digits)):
                #숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # 예외 처리
        if not digits:
            return []
        
        dic = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }
        result=[]
        dfs(0, "")
        
        return result

        # dictionary 개선
        # mine
        if len(digits) == 0:
            return []
        
        key_map = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }
        res = []
        def btr(digits:str, string:str=''):
            if digits == '':
                res.append(string)
                return
            for char in key_map[digits[0]]:
                btr(digits[1:], string+char)
        btr(digits)
        return res

        # mine
        # 1. 기껏해야 digits는 4개가 끝임 -> brute-force로 풀어보자
        if len(digits) == 0:
            return []
        
        key_map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r', 's'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        res = []
        def btr(digits:str, string:str=''):
            if digits == '':
                res.append(string)
                return
            for char in key_map[digits[0]]:
                btr(digits[1:], string+char)
        btr(digits)
        return res
            
            

