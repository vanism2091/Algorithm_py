from typing import *
# https://leetcode.com/problems/merge-two-sorted-lists/
# 다시보자!!!!
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 다른 풀이
        a = list1
        b = list2
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

        # sol_1-book: recursion
        if not list1 or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
        
        # mine... 몰루... :( linked list 주소값 빡취네...
        if not list1 or not list2:
            return list1 or list2

        pivot1, pivot1.next, pivot2, pivot2.next = list1, list1, list2, list2

        while pivot1.next and pivot2.next:
            if pivot1.next.val > pivot2.next.val:
                pivot1.next, pivot1.next.next, pivot2 = pivot2.next, pivot1.next, pivot2.next
            pivot1 = pivot1.next
        if pivot2.next:
            pivot1.next = pivot2.next
        return list1    
                
