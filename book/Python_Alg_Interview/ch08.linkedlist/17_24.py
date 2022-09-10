from typing import *
# https://leetcode.com/problems/swap-nodes-in-pairs/
# 24. Swap Nodes in Pairs
"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sol_3-book recursive
        # 내가 한 것과 동일하므로 새로 돌리지는 않을 예정.
        # 반복 풀이와 달리, 포인터 역할을 하는 변수는 p만 있으면 됨 (반복은 root, prev, b)
        # 더미 노드를 만들 필요도 없음. 공간 복잡도가 더 낮음.
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
        
        # sol_3-b_mine recursive
        # 40ms
        if not head or not head.next:
            return head
        b = head.next
        head.next = self.swapPairs(b.next)
        b.next = head
        return b

        # sol_2-book 반복 구조로 스왑
        # 나보다 좋은 점: 나는 slow, fast 두 개를 썼는데, 여기선 b 하나만 씀. 
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b -> a(head)
            b = head.next
            head.next = b.next
            b.next = head

            # prev -> b
            prev.next = b

            # 다음 비교를 위해 이동
            prev, head = prev.next.next, head.next
            # prev, head = head, head.next.next
            # 직접 손으로 써가며 비교해보니, prev = head는 ok 그러나 head <- head.next가 맞음
        return root.next
        
        # sol_1-book 값만 교환(문제에서 요구한 방식 아님)
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head
            
        
        # mine
        # fast, slow로 풀 수 있을 것 같은..?
        root = start = ListNode(next=head)
        while start and start.next:
            slow, fast = start.next, start.next.next
            slow.next = fast.next
            fast.next = slow
            start = slow
        return root.next

    # mine
    # fast, slow로 풀 수 있을 것 같은..?