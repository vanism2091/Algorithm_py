import collections
from typing import *
# https://leetcode.com/problems/design-circular-queue/
# book
# 나는 front는 다음 칸을 가리키게 했는데, 여긴 있는 칸을 가리킴
class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
        
    # enQueue(): rear 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # deQueue(): front 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.k
        return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        # 이렇게 그냥 -1 해도 되는게, 어차피 0 - 1 = -1이고 q[-1] = last element임
        return -1 if self.q[self.p2 - 1] else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.q[self.h] is None

    def isFull(self) -> bool:
        return self.q[self.t] is not None


# mine2: list로
# isEmpty()에서
# return not ~ 하니까 value가 0일때도 True 리턴돼서 틀렸었음. int value type 이면 걍 is None 으로 하는게 나을듯? 
class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.k = k
        self.h = 0
        self.t = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.t] = value
        self.t = (self.t + 1) % self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.h] = None
        self.h = (self.h + 1) % self.k
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.h]

    def Rear(self) -> int:
        r_idx = self.t - 1 if self.t > 0 else self.k - 1
        return -1 if self.isEmpty() else self.q[r_idx]

    def isEmpty(self) -> bool:
        return self.q[self.h] is None

    def isFull(self) -> bool:
        return self.q[self.t] is not None


# mine1
# 근데 문제가 deque 쓰지 말라함 :)
# You must solve the problem 
# without using the built-in queue data structure 
# in your programming language. 
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = collections.deque()
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.append(value)
        pass

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        return self.q.popleft()

    def Front(self) -> int:
        return self.q[0]

    def Rear(self) -> int:
        return self.q[-1] 

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()