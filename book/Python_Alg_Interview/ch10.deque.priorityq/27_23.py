import heapq
from typing import *
# https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # sol_1-book
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # 힙 추출 후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        
        return root.next

        # mine
        # heappush 시 val이 같으면 2번째 요소로 비교함
        # 그런데 ListNode와 ListNode는 비교할 수 없음
        # * 방법 1 
        # ListNode 클래스에 아래 함수를 구현
        #   * __lt__(self, other) for <
        #   * __le__(self, other) for <=
        # * 방법 2 (채택) 
        # id(l)을 튜플의 두 번째 요소로 추가 - 비교 기준을 추가
        # https://docs.python.org/3/library/heapq.html 
        # https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances
        if not lists:
            return None
        hq = []
        root = node = ListNode()
        for l in lists:
            if l is None:
                continue
            heapq.heappush(hq, (l.val, id(l), l))
        while hq:
            _, _, curr = heapq.heappop(hq)
            node.next = curr
            # 연결하기
            if curr.next is not None:
            # if curr.next:
                heapq.heappush(hq, (curr.next.val, id(curr.next), curr.next))
            node = node.next
        return root.next

            