
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
끝말잇기는 다음과 같은 규칙으로 진행됩니다.
 - 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
 - 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
 - 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
 - 이전에 등장했던 단어는 사용할 수 없습니다.
 - 한 글자인 단어는 인정되지 않습니다

n : 끝말잇기에 참여하는 사람 [2, 10]
words: 끝말잇기에 사용한 단어들 : [n, 100]

"""
# 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981?language=python3
def solution(n, words):
    words_set = set([words[0]])
    for i, word in enumerate(words[1:], start=1):
        if word in words_set or words[i-1][-1] != word[0]:
            return [i%n + 1, i//n + 1]
        words_set.add(word)
    return [0,0]

examples = [[3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'], [3, 3]], [5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive'], [0, 0]], [2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'], [1, 3]]]

test_cases(solution, examples)

"""

set 굳이 안만들고 이렇게 하면 space complexity 측면에서 좋을듯
words[p] in words[:p]
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12981/solution_groups?language=python3
def others():
    def solution(n, words):
        for p in range(1, len(words)):
            if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
        return [0,0]



