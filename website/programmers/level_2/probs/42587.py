
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
중요도가 높은 문서를 먼저 인쇄하는 프린터
인쇄 방식
    1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
    2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
    3. 그렇지 않으면 J를 인쇄합니다.
e.g.
문서 (A, B, C, D) 중요도 (2, 1, 3, 2)
1. A 꺼냈는데 C가 있으니까 A는 맨 뒤로, 마찬가지로 B 맨 뒤로
2. C(3) 꺼낸 후 인쇄, 그 후 D, A, B
즉, C D A B
문서의 순서에 따라 같은 중요도의 문서 간에 위치가 달라지겠다.

제한 사항
#docs : [1, 100]
priority: [1, 9], bigger == more important
location [0,#docs-1]

priorities: [2, 1, 3, 2]	location: 2	
return: 1

1,2,3,1,2,4,3,2,1,3
4,3,2,1,3, 1,2,3,1,2
일단 그대로 구현을 해보자... :(
"""
# 프린터
# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3
from collections import deque
from collections import Counter

def solution(priorities, location):
    answer = 0
    p_cnt = Counter(priorities)
    q = deque([(p, i) for i,p in enumerate(priorities)])
    curr_max = max(p_cnt)
    num_max = p_cnt[curr_max]
    while q:
        c_pri, c_idx = q.popleft()
        if c_pri == curr_max:
            answer += 1
            num_max -= 1
            if location == c_idx:
                return answer
            if num_max == 0:
                del p_cnt[curr_max]
                curr_max = max(p_cnt)
                num_max = p_cnt[curr_max]
        else:
            q.append((c_pri, c_idx))
    return answer

"""
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.10ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.1MB)
테스트 6 〉	통과 (0.07ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.09ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.10ms, 10MB)
테스트 11 〉	통과 (0.08ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.1MB)
테스트 13 〉	통과 (0.07ms, 10.1MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.1MB)
테스트 16 〉	통과 (0.04ms, 10.3MB)
테스트 17 〉	통과 (0.09ms, 10.2MB)
테스트 18 〉	통과 (0.05ms, 10.2MB)
테스트 19 〉	통과 (0.07ms, 10.2MB)
테스트 20 〉	통과 (0.06ms, 10.1MB)

위 코드를 더 단순화시킬 수 있을 것 같은데, 그럼 시간이 늘어날진 모르겠다.
더 고민해보자.
"""



examples = [[[2, 1, 3, 2], 2, 1], [[1, 1, 9, 1, 1, 1], 0, 5]]

test_cases(solution, examples)

"""
any 함수!!!
>>> any([False, False, False])
False
>>> any([False, True, False])
True
>>> all([False, True, False])
False
>>> all([True, True, True])
True
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42587/solution_groups?language=python3
def others():
    def solution(priorities, location):
        queue =  [(i,p) for i,p in enumerate(priorities)]
        answer = 0
        while True:
            cur = queue.pop(0)
            if any(cur[1] < q[1] for q in queue):
                queue.append(cur)
            else:
                answer += 1
                if cur[0] == location:
                    return answer



