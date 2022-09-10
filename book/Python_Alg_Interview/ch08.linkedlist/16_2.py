from typing import *
# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # sol_2-book : not recursion but iterative
        # 182 ms
        # - divmod!!!!
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = carry
            # 두 입력 값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next

        
        # sol_2-b_mine : 전가산기 구현
        # 124 ms
        def adder(l1, l2, carry=0) -> Optional[ListNode]:
            sum = carry
            if not l1 and not l2:
                return ListNode(sum) if carry else None
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, sum = sum // 10, sum % 10
            node = ListNode(sum)
            node.next = adder(l1, l2, carry)
            return node
        return adder(l1, l2)
        # sol_1-book : 이건 근데 우아한 풀이가 아님
            # 연결리스트 뒤집기
            # 문자열로 이어붙인 후 숫자로 변환
            # 합 계산 후 다시 리스트로 바꾸기
        # 연결 리스트 뒤집기
        def reverse_list(head:ListNode) -> ListNode:
            node, prev = head, None

            while node:
                next, node.next = node.next, prev 
                node, prev = next, node
            return prev
        # 연결 리스트 파이썬 리스트로 변환
        def to_list(node:ListNode) -> list:
            li: list = []
            while node:
                li.append(node.val)
                node = node.next
            return li
        # 파이썬 리스트 -> 연결 리스트
        def to_reversed_linked_list(result:list) -> ListNode:
            prev: ListNode = None
            for r in result:
                node = ListNode(r)
                node.next = prev
                prev = node
            return node
        # 두 연결 리스트의 덧셈
        
        n1 = to_list(reverse_list(l1))
        n2 = to_list(reverse_list(l2))
        result_str = int(''.join(map(str,n1))) \
            + int(''.join(map(str,n2)))
        return to_reversed_linked_list(str(result_str))

        # sol_1 제목(자료형 변환)을 본 내 풀이
        # 160ms
        def to_number(node:Optional[ListNode], num:int=0, exp:int=0) -> int:
            if not node:
                return num
            return to_number(node.next, num + node.val * (10**exp), exp+1)
        def to_list(num:int)->ListNode:
            next = None
            for digit in map(int, str(num)):
                node = ListNode(digit, next)
                next = node
            return node
                
        return to_list(to_number(l1) + to_number(l2))
        

        # 최적화해보기 1
        # 129 ms
        # 첫 번째 elif 괄호가 없으면, l2가 있기만 하면 조건문이 참이 됨
        # 캐리가 있고, l1 또는 l2가 있을 때: 이 의도라면 괄호가 있어야 함. 주의!!
        # 첫 번째 친구와 두 번째 친구를 통합하는 방법은 없을까? if, elif문.
        def add(l1:Optional[ListNode], l2:Optional[ListNode], carry:int = 0)->Optional[ListNode]:
            if l1 and l2:
                val_sum = l1.val + l2.val + carry
                l1.val = val_sum % 10
                l1.next = add(l1.next, l2.next, val_sum // 10)
            elif carry and (l1 or l2):
            # elif carry and l1 or l2:
                k = l1 or l2
                k.val = (k.val + carry) % 10
                k.next = add(k.next, None, k.val==0)
            elif not l1 and not l2:
                return ListNode(1) if carry else None
            return l1 or l2
        return add(l1, l2)

        # mine 코드 정리 전
        def add(l1:Optional[ListNode], l2:Optional[ListNode], carry:int = 0)->Optional[ListNode]:
            if carry:
                if l1 and l2:
                    val_sum = l1.val + l2.val + carry    
                    l1.val = val_sum % 10
                    l1.next = add(l1.next, l2.next, val_sum // 10)
                elif l1 or l2:
                    k = l1 or l2
                    k.val = 0 if k.val == 9 else k.val + 1
                    k.next = add(k.next, None, k.val==0)
                else:
                    return ListNode(1)
            elif l1 and l2: # carry 없고 l1과 l2가 있는 경우
                val_sum = l1.val + l2.val
                l1.val = val_sum % 10
                l1.next = add(l1.next, l2.next, val_sum // 10)
            return l1 or l2
        return add(l1, l2)

        """ mine (통과)
        # mine 연결 리스트 특성을 활용해 1개씩 더라고 캐리 올리는 식으로 풀고싶음..
        # carry true / false
        # l1 true / false
        # l2 true / false

        # 한 번에 처리 가능
        # 111 -> 캐리까지 더함
        # 110 -> 캐리 빼고 더함

        # 101, 100 -> 캐리 더하고 이후는 그냥 끝
        
        # 011, 010 -> l2 -> l1으로 바꾸고 캐리 더하고 return 그냥 끝

        # 001 -> return 새 리스트 노드
        # 000 -> None

        # ㅇㅋ 일단 이거 되는거 확인완
        def add(l1:Optional[ListNode], l2:Optional[ListNode], carry:int = 0)->Optional[ListNode]:
            if carry:
                if l1 and l2:
                    val_sum = l1.val + l2.val + carry    
                    l1.val = val_sum % 10
                    l1.next = add(l1.next, l2.next, val_sum // 10)
                elif l1 or l2:
                    k = l1 or l2
                    k.val = 0 if k.val == 9 else k.val + 1
                    k.next = add(k.next, None, k.val==0)
                else:
                    return ListNode(1)
            elif l1 and l2: # carry 없고 l1과 l2가 있는 경우
                val_sum = l1.val + l2.val
                l1.val = val_sum % 10
                l1.next = add(l1.next, l2.next, val_sum // 10)
            return l1 or l2
        return add(l1, l2)
        """



# [2,4,3]
# [5,6,4]
# [1,8]
# [0]