from typing import *

# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sol_1-book: iterative
        # 94 ms
        # Odd는 odd끼리, even은 even끼리.
        # 다 하면, odd 뒤에 even 연결
        if not head:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head
        
        # mine: iterative
        if not head or not head.next or not head.next.next:
            return head
        root = ListNode(next=head)
        p = head.next
        while p and p.next:
            p_next = p.next
            p.next = p_next.next
            p_next.next = head.next
            head.next = p_next
            # 다음 루프를 위한 이동
            head, p = head.next, p.next
        return root.next
