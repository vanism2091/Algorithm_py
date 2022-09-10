from typing import *
import collections
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # sol_3 -book using runner
        # 내가 직접 할때 발생했던 문제. slow를 바로 rev에 넣으면 같은 참조가 되는 것
        # 그러나 책 풀이처럼 다중할당을 이용하면 한 번에 처리되기 때문에 풀 수 있음
        # rev, rev.next = slow, rev
        # slow = slow.next 
        # 이 경우, slow.next는 (첫 번째 노드일 때) None이 된다 :(
        # rev, rev.next, slow = slow, rev, slow.next
        # 딱 그 시점의 값을 할당... a, b = b, a 가 되는 것과 같은 원리
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

        # sol_3 - using runner
        # Fast runner, slow runner
        # Fast가 끝에 도달할 때, slow는 중간에 도달. 
        # 따라서 Fast가 끝에 도달할 때 까지 slow는 역순으로 연결 리스트 rev를 만들고
        # Fast가 도달한 후에는 rev와 남은 절반이 일치하는지 체크 
        # 2688 ms
        rev = None
        fast = slow = head
        while fast and fast.next:
            # build rev
            fast = fast.next.next
            temp = ListNode(val=slow.val, next=rev)
            rev = temp
            slow = slow.next
        
        slow = slow.next if fast else slow
        while rev:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next
        return True
        
        # sol_2-book optimize 1 using deque
        # 아래와 유사
        
        # sol_2 - mine
        q: Deque = collections.deque()        
        if not head:
            return True
        
        node = head
        # 리스트로 변환
        while node:
            q.append(node.val)
            node = node.next
            
        # 팰린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
        
        # sol_1-book convert to list 
        # q.pop(0) -> O(n)
        # O(n**2)
        q: list = []

        if not head:
            return True
        node = head
        # convert to list
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # check palindrome
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True

        # mine
        # O(n) time, but O(n) space
        vals = []
        while head.next:
            vals.append(head.val)
            head = head.next
        vals.append(head.val)
        return vals == vals[::-1]