import collections
from typing import *
# https://leetcode.com/problems/design-circular-deque/

# sol_1-book
# 다중 할당시 내가 생각한대로 동작이 안되는 듯. 추후 디버깅해보자
class ListNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.head.right, self.tail.left = self.tail, self.head
        self.maxlen, self.len = k, 0

    # 얘는 안되나
    # def _add(self, prev:ListNode, next:ListNode):
        # next.left, next.right = prev, prev.right
        # prev.right.left, prev.right = next, next
    def _add(self, node:ListNode, new:ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    
    def _del(self, node:ListNode):
        n = node.right.right
        node.right, n.left = n, node

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True


    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.right.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.left.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.maxlen == self.len




# sol_1-b_mine: 이중 연결 리스트를 이용한 데크 구현
class Node:
    def __init__(self, item=0, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
class MyCircularDeque:
    def __init__(self, k: int):
        self.head = Node()
        self.tail = Node(left=self.head)
        self.head.right = self.tail
        self.maxlen = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(item=value, left=self.head, right=self.head.right)
        self.head.right.left, self.head.right = node, node
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(item=value, left=self.tail.left, right=self.tail)
        self.tail.left.right, self.tail.left = node, node
        self.length += 1
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head.right.left, self.head.right = self.head, self.head.right.right
        # 메모리에서 지워야???
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail.left.left.right, self.tail.left = self.tail, self.tail.left.left
        self.length -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.right.item

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.left.item

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.maxlen == self.length



# mine2: use list
class MyCircularDeque:
    def __init__(self, k: int):
        self.q = [None] * k
        self.k = k
        self.h = 0
        self.t = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.h = self.__prevIdxOf(self.h)
        self.q[self.h] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.t] = value
        self.t = self.__nextIdxOf(self.t)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.h] = None
        self.h = self.__nextIdxOf(self.h)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.t = self.__prevIdxOf(self.t)
        self.q[self.t] = None
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.q[self.h]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.__prevIdxOf(self.t)]

    def isEmpty(self) -> bool:
        return self.q[self.h] is None

    def isFull(self) -> bool:
        return self.q[self.t] is not None
    
    def __nextIdxOf(self, idx) -> int:
        return (idx + 1) % self.k
    
    def __prevIdxOf(self, idx) -> int:
        return idx - 1 if idx > 0 else self.k - 1


# mine1: use deque
class MyCircularDeque:
    def __init__(self, k: int):
        self.q = collections.deque()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q.pop()
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.q[0]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.q[-1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
