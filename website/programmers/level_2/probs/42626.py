
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
모든 스코빌 지수를 k 이상 만득고싶다.
가장 스코빌 지수가 낮은 두 개의 음식을 섞어 새로운 방법을 만든다.
섞은 음식의 스코빌 지수 
    = 가장 맵지 않은 음식의 스코빌 지수 
        + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
모든 스코빌 지수가 k이상 될때까지 반복해서 섞는다.

섞어야 하는 최소 횟수는?

constraint
 len(스코빌) [2, 1_000_000]
 k: [0, 1_000_000_000]
 scoville_i [0, 1_000_000]
 모든 음식의 스코빌 지수를 k이상으로 만들 수 없는 경우에는 -1을 리턴한다.

 [1, 2, 3, 9, 10, 12]	7	2
 1) K보다 작은 친구만 남긴다.

 힙큐를 사용하자
 1. 힙큐에 K보다 작은 애들 때려넣고
 2. heappop하면 알아서 미니멈부터 나옴
 3. 2개 꺼내고 새로운 음식 만들어서 K보다 작으면 넣고, 크면 컨티뉴
 4. sq에 음식이 1개만 남아있으면 -1
"""
import heapq
# 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while any([s < K for s in scoville]):
        if len(scoville) == 1:
            return -1
        s1, s2 = heapq.heappop(scoville), heapq.heappop(scoville)
        new = s1 + s2*2
        if new < K:
            heapq.heappush(scoville, new)
        answer += 1
    return answer


"""
1차...
정확성 4개 틀림, 효율성 통과
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 9.87MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10MB)
테스트 5 〉	통과 (0.01ms, 10MB)
    테스트 6 〉	실패 (0.44ms, 10.2MB)
    테스트 7 〉	실패 (0.42ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
    테스트 10 〉	실패 (0.34ms, 10MB)
테스트 11 〉	통과 (0.21ms, 9.96MB)
테스트 12 〉	통과 (0.90ms, 10.2MB)
    테스트 13 〉	실패 (0.37ms, 10MB)
테스트 14 〉	통과 (0.02ms, 10.1MB)
테스트 15 〉	통과 (0.49ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
"""
# 2차..
# 스코빌 전체.. - 모든 음식 섞
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # while any([s < K for s in scoville]):
    while scoville[0]<K:
        if len(scoville) == 1:
            return -1
        s1, s2 = heapq.heappop(scoville), heapq.heappop(scoville)
        new = s1 + s2*2
        # if new < K:
        heapq.heappush(scoville, new)
        answer += 1
    return answer

examples = [[[1, 2, 3, 9, 10, 12], 7, 2], [[2, 1, 1],14, -1] ]

test_cases(solution, examples)

"""
1. pushpop
"""
# https://school.programmers.co.kr/learn/courses/30/lessons/42626/solution_groups?language=python3
def others():
    import heapq

    def solution(scoville, K):
        heapq.heapify(scoville)
        size, cnt = len(scoville) - 1, 0
        f = heapq.heappop(scoville)
        while size > 0:
            s = heapq.heappop(scoville)
            f = heapq.heappushpop(scoville, f + s + s)
            if f >= K:
                return cnt + 1
            cnt += 1
            size -= 1
        return -1

"""
코드들을 보니 다들 import heapq를 하셨는데 저는 heap을 몰라서..ㅎㅎ 
queue만 써서 풀었는데도 시간이 heap을 쓴 풀이의 절반 정도 걸리네요. 
저는 섞어서 나온 새로운 값, mix들을 별도의 queue에 넣었는데 이게 가장 큰 요인같네요.
나중에 나온 mix값이 먼저 나온 것보다 클 수밖에 없어서 섞는 순서대로 
queue에 넣어주면 크기 순서를 신경 쓸 필요가 없어요. 
그냥 popleft로 꺼내면 무조건 mix값의 최소입니다ㅎ
"""

