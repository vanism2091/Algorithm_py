import collections
from typing import *
# https://leetcode.com/problems/design-hashmap/


########################################################
# sol_1-book : chaining
# 왜 내껀 안되고 이건 됐을까
# 차이는 defaultdict와 list 여부인데, 아래 풀이를 list로 바꿔서 돌려볼까...
# 책 코드 list로 바꿔도 되는데요..?
# 하.... put while문에서 next로 넘기는 코드를 빼먹음ㅋㅋㅋㅋㅋㅋㅋㅋ
# TODO: Linear Probing으로도 구현해보기
########################################################
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1_000
        self.table = collections.defaultdict(ListNode)

    # 삽입

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            # 첫 루프에는 prev==p이지만, 그 경우는 위에서 제거했음.
            # 이 부분이 거슬린다면 직접 개선해볼것
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


########################################################
# sol_1-book : chaining
# Defaultdict -> list
########################################################
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1_000
        self.table = [None] * self.size

    # 삽입

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index] is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index] is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index] is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            # 첫 루프에는 prev==p이지만, 그 경우는 위에서 제거했음.
            # 이 부분이 거슬린다면 직접 개선해볼것
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

# mine - chaining
# Time limit :(
# 꼼꼼히..!


class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.val = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.table_size = 1000
        self.table = [None] * self.table_size

    def put(self, key: int, value: int) -> None:
        hash_value = key % self.table_size
        node = self.table[hash_value]
        while node:
            if node.key == key:
                node.value = value
                return
            # 아래 친구를 빼먹어서 타임 리미트에 걸렸던것.... ㅂㄷㅂㄷㅂㄷ
            # while문에서 문제가 있을 줄은 알았지만 :(
            node = node.next
        else:
            self.table[hash_value] = ListNode(
                key, value, self.table[hash_value])

    def get(self, key: int) -> int:
        node = self.table[key % self.table_size]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        hash_value = key % self.table_size
        node = self.table[hash_value]
        if node is None:
            return
        if node.key == key:
            self.table[hash_value] = node.next
            return

        prev = node
        while node:
            if node.key == key:
                prev.next = node.next
                return
            prev, node = node, node.next


"""
class MyHashMap:

    def __init__(self):
        

    def put(self, key: int, value: int) -> None:
        

    def get(self, key: int) -> int:
        

    def remove(self, key: int) -> None:
"""


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
