from typing import *
# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # sol_1-book : iterative
        # - 예외 처리 및 빠른 리턴
        # - next 이후이후이후는 알 바 아니고,
        #   엮여 있는 것들 바꾸면 알아서 엮인 것들이 바뀐다...
        if not head or left==right:
            return head

        root = start = ListNode(next=head)
        #start, end 지정
        for _ in range(left - 1):
            start = start.next
        end = start.next
        
        for _ in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp
        return root.next


        # sol_1-b_mine : iterative
        root = start = ListNode(next=head)
        for _ in range(left - 1):
            start = start.next
        end, temp = start.next
        for _ in range(right - left):
            start.next, end.next = end.next, end.next.next
            # 아래 친구를 하면 안됨. 연결 리스트의 특성을 잊지 말자 :)
            # temp.next = end
            start.next.next, temp = temp, start.next
        return root.next
        
        # mine
        root = node = ListNode(next=head)
        for _ in range(left - 1):
            node = node.next
        before_left_node, left_node, node, prev = node, node.next, node.next, None
        for _ in range(right - left + 1):
            next, node.next = node.next, prev
            prev, node = node, next
        left_node.next = node
        before_left_node.next = prev
        return root.next

        # mine - Fail
        # [3, 5] , 1, 2 했을 때, [3]만 나옴.
        # 첫 루프때 node(head).next = prev 하면서, head.next가 None이 되어버림.
        node = ListNode(next=head)
        for _ in range(left - 1):
            node = node.next
        before_left_node, left_node, node, prev = node, node.next, node.next, None
        for _ in range(right - left + 1):
            next, node.next = node.next, prev
            prev, node = node, next
        left_node.next = node
        before_left_node.next = prev
        return head

s = Solution()
def list_to_ll(l:list)->ListNode:
    prev: ListNode = None
    for e in l:
        n = ListNode(val=e, next=prev)
        prev = n
    return n

print(s.reverseBetween(head=list_to_ll([5,3]), left=1, right=2))

"""
[1,2,3,4,5]
2
4
[5]
1
1
"""