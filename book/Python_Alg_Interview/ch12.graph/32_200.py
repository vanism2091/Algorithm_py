from re import X
from typing import *
# https://leetcode.com/problems/number-of-islands/

"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output = 1
"""


class Solution:
    # sol_1-book-2: 중첩함수
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = '0'
            # 동서남북 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count

    # sol_1-book-1:
    # 별도의 visited 배열을 생성할 경우 공간 복잡도가 증가. 이 문제는 새로 생성하지 않아도 풀 수 있음

    grid: List[List[str]]  # 클래스 멤버 변수로 선언

    def dfs(self, i: int, j: int):
        # 더 이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(self.grid) or \
                j < 0 or j >= len(self.grid[0]) or \
                self.grid[i][j] != '1':
            return

        self.grid[i][j] = '0'
        # 동서남북 탐색
        self.dfs(i+1, j)
        self.dfs(i-1, j)
        self.dfs(i, j+1)
        self.dfs(i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        # 예외 처리
        if not grid:
            return 0

        self.grid = grid

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1

        return count

        # mine: 책 앞 부분 조금 참고.. :)
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        cnt = 0
        y_len, x_len = len(grid), len(grid[0])

        def dfs(y, x):
            if 0 <= x < x_len \
                and 0 <= y < y_len \
                    and grid[y][x] == '1':
                grid[y][x] = '0'
                for i in range(4):
                    dfs(y + dy[i], x+dx[i])

        for y in range(y_len):
            for x in range(x_len):
                if grid[y][x] == '1':
                    dfs(y, x)
                    cnt += 1
        return cnt


def outer_func(a: List[int]):
    b: List[int] = a
    print(id(b), b)

    def inner_func_1():
        b.append(4)
        print(id(b), b)
    
    def inner_func_2():
        b = [3, 4, 5]
        print(id(b), b)

    def inner_func_3():
        print(id(b), b)
    
    
    inner_func_1()
    inner_func_2()
    inner_func_3()


outer_func([1, 2, 3])

