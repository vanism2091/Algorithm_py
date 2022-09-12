import collections
from typing import *
# https://leetcode.com/problems/implement-stack-using-queues/

# sol_1-book
# 넣을 때마다 정렬 -> top, pop 더 간편해짐
# q를 1개만 쓸 수 있음 append+popleft
class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# mine
class MyStack:

    def __init__(self):
        self.q1:Deque = collections.deque()
        self.q2:Deque = collections.deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        pass

    def pop(self) -> int:
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        last = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return last

    def top(self) -> int:
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        last = self.q1.popleft()
        self.q2.append(last)
        self.q1, self.q2 = self.q2, self.q1
        return last

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()