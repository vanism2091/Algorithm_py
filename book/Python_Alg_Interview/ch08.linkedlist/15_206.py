from typing import *
# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sol_2-book
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
        
        # sol_2 1을 참고한 mine
        if not head:
            return head
        prev = None
        node = head
        while True:
            next, node.next = node.next, prev
            prev, node = node, next
            if not next:
                break
        return prev

        # sol_1-book recursion
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)
        # 아래 처럼 하면 Error - Found cycle in the ListNode 동일한 에러가 또 발생
        # return reverse(head.next, head)
        
        # mine
        # Error - Found cycle in the ListNode
        if not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        return res