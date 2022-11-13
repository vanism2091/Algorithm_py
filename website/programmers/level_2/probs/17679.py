
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

"""
# [1차] 프렌즈4블록
# https://school.programmers.co.kr/learn/courses/30/lessons/17679?language=python3
import numpy as np

def solution(m, n, board):
    # 1. init    
    m, n = 4, 5
    characters = ("R", "M", "A", "F", "N", "T", "J", "C")
    board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
    t_board = np.array([ list(s) for s in board]).transpose()
    t_board = ["".join(l.tolist()) for l in t_board]
    t_board
    total = 0
    top_idx = [0] * n
    continued = True
    while continued:
        pos = set()
        # check
        for i in range(m-1):
            for j in range(n-1):
                char_set = set(board[i][j:j+2]+board[i+1][j:j+2])
                if len(char_set) == 1 and char_set[0] in characters:
                    # pos 에 넣기
                    pass       
        check = len(pos)
        if checked == 0:
            break
        total += checked

        

    print(check_board)

    answer = 0
    return answer

examples = [[4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF'], 14], [6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'], 15]]

test_cases(solution, examples)

"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/17679/solution_groups?language=python3
def others():
    pass



