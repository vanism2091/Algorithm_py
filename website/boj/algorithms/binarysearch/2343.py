
"""
input:
    N: lecture 개수 
    M: 블루레이 개수
    lectures [1, 10000)
output:
    가능한 블루레이 크기 중 최소

내 생각
    찾는 target은 "블루레이의 길이"로 하자
    그때마다 강의 리스트를 순회하면서 블루레이의 갯수를 카운트하고 (O(L))
    cnt가 M(가능한 블루레이의 갯수)보다 크다면
        블루레이 길이가 짧은 것이므로 
        start = mid + 1
    cnt <= M 이면,
        cnt가 M보다 작거나 같으면 현재 mid를 기록한다.
        블루레이 길이가 최소 길이보다 더 길거나 같기 때문에 
        최소 블루레이 길이를 찾기 위해, end = mid+1
        "최소"를 찾기 때문에 등호는 여기에 붙인다.
    서치가 끝난 후 최종 기록된 mid가 정답

1차. 
    start = 0
    end = 10000 
2차. / 3차.
    start = max(lectures)
    end = 10000 / 10001
    -> NameError
    answer가 정의가 안된듯
4차.
    answer을 while 전에 정의했고, 틀림
5차.
    start = max(lectures)
    end = int(1e9)

    1)
        start 는 0이 아니라 max(lectures)
    2) 
        end를 바꿨다. 블루레이 길이는 강의 여러개가 들어갈 수 있으므로 최대 (강의 수*강의 길이)인데,
        처음 풀 때 이를 놓쳤다 :)
    이진 탐색은 다음을 꼭 주의하자.
        뭘 탐색할지, 
        start, end를 어떻게 정의할지
        등호는 어디에 붙일지

"""

# 기타 레슨
# https://www.acmicpc.net/problem/2343
# 42132	816
from bisect import bisect_right


def sol_2343():
    N, M = map(int,input().split())
    lectures = list(map(int, input().split()))

    start = max(lectures)
    end = int(1e9)
    answer = start
    while start <= end:
        mid = (start+end)//2
        
        cnt = 1
        curr_sum = lectures[0]
        for lecture in lectures[1:]:
            if curr_sum + lecture > mid:
                curr_sum = lecture
                cnt += 1
            else:
                curr_sum += lecture
            if cnt == M+1:
                break
        if cnt <= M:
            answer = mid
            end = mid-1
        else: # cnt >= M
            start = mid + 1

    print(answer)
    pass


"""
다른 분 풀이에서 배울 점
1. input 처리
    sys.stdin.read 로 한 줄로 깔끔하게 함
로직:
    - lectures의 max와 sum을 구한다. (-> start, end)
    - lectures의 누적 합을 구한다.
        - [1번째 강의, 강의1+2, 강의1+2+3, ..., 강의 1+2+...+n]
    - simulate 함수
        - 0, ..., m-1번까지
            - sub = seq[bisect_right(seq, size + sub) - 1]
                - seq: 누적합, size: mid, sub: 0부터 반복문 돌며 할당된다
                - sub:0일때, seq에서 size가 들어갈 index를 반환한다.
                    - 그 후, sub는 그 직전 index의 값이 된다.
                    - 즉, 첫 번째 블루레이까지의 길이가 됨.
            - sub == seq[-1]: sub가 누적 합의 마지막일때,
                즉 모든 강의가 m개 이하의 블루레이 안에 담겼을 때 break
        - 반복문이 종료된 후, 위의 조건문을 다시 체크한 후,
            참이면 True, 거짓이면 False를 반환한다.
            참 == 모든 강의가 m개 이하의 블루레이 안에 담겼다
    - simulate 가 True면 
        end = mid -1, 탐색 범위를 왼쪽으로 좁힌다.
    - False면, 탐색 범위를 오른쪽으로 좁힌다.

    - 최종은 e+1을 리턴한다.
        - 이렇게 하면 별도의 변수를 선언하지 않아도 되겠다.
2. 로직에서 배울 점
    1. 강의 시간 누적 합을 구한 후, 오름차순으로 정렬된 강의 누적합에서
        bisect_right로 바로 index를 구한다.
        나는 bs할때마다 O(N)의 시간이 소요됐는데, 이 답은 O(MlogN) 이하 (M <= N)
    2. answer을 따로 선언, 할당하지 않고 bs 끝나면 e+1을 리턴
    3. end point는 sum(seq)
        int(1e9) 보다 훨씬 합당하다
3. if __name__ == '__main__':
        print(sol2343())
    이 방식 좋은 듯 써먹어야지 :)
4. sys.stdin.read / readline / readlines 차이 명확하게 공부해보자
"""
# 42300	116
# https://www.acmicpc.net/problem/status/2343/1003/1
def other_2343():
    import sys
    from bisect import bisect_right

    input = sys.stdin.read


    def sol2343():
        n, m, *seq = map(int, input().split())
        s, e = max(seq), sum(seq)
        for i in range(n - 1):
            seq[i + 1] += seq[i]
        while s <= e:
            mid = (s + e) // 2
            if simulate(seq, mid, m):
                e = mid - 1
            else:
                s = mid + 1
        return e + 1


    def simulate(seq, size, m):
        sub = 0
        for _ in range(m):
            sub = seq[bisect_right(seq, size + sub) - 1]
            if sub == seq[-1]:
                break
        return True if sub == seq[-1] else False


    if __name__ == '__main__':
        print(sol2343())


# 다른 분 풀이 복기하며 다시 풀어보는 sol_2343
import sys
from bisect import bisect_right

def sol_2343():
    input = sys.stdin.read

    n, m, *lectures = map(int,input().split())
    start, end = max(lectures), sum(lectures)
    # n이 주어져있으므로 len(lecture)을 쓸 필요가 없음
    for i in range(1, len(lectures)):
        lectures[i] += lectures[i-1]

    while start <= end:
        mid = (start+end)//2
        if is_possible(lectures, mid, m):
            end = mid - 1
        else:
            start = mid + 1
    return end + 1

def is_possible(ls, l, m):
    sub = 0
    for _ in range(m):
        sub = ls[bisect_right(ls, l+sub)-1]
        if sub == ls[-1]:
            break
    return True if sub == ls[-1] else False

if __name__ == '__main__':
        print(sol_2343())



"""
또 다른 분
1. input은 내가 아는 대로.
2. INF, r은 왜 _?
    파이썬은 숫자 또는 문자값의 자릴수 구분을 위한 구분자로 _ 를 쓸 수 있다. 오..!
3. 이 코드에서의 변수명
    arr: lectures
    l : start
    r : end
    ans: answer / r+1 로 초기화
4. ans 찾는 여정
    1. arr 누적합 리스트 만들기
    2. bs
        m : mid
        count = 1
        accum = m
        idx = acuum이 누적합에 들어갈 왼쪽 idx
        - count < M 일 때 까지,
            종료 조건 : cnt < M or idx == N
                블루레이 갯수가 M보다 커지거나, idx가 N일때 (즉, 모든 강의가 블루레이에 담겼을 때)
            - idx > 0: bisect_left 한 결과가 0보다 크다면
                accum = arr[idx-1] + m
            - 그렇지 않으면, idx == 0이다. 즉 min(*arr, acc) 은 acc이다.
                accum += m?
                이 경우는 논리적으로 그냥 break 하는게 맞지 않나?
                애초에 start가 max(lectures)인데 가능한가?
요약
- 강의 재생시간 누적합 구하기
- 숫자 자리수 구분 시 _ 사용 가능
- idx <- bisect_left 최대 M번 해서, 최종 idx가 N인 경우,
    == 길이 mid의 블루레이 m개로 마지막 강의까지 모두 담을 수 있는 경우
    ans = min(ans, m-1)
        왜 m-1이지?
        으음... 나중에 다시 생각해보자
"""
# 	44096	128
def another_2343():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline

    INF = 1_000_000_000
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    l = max(arr)
    r = 1_000_000_001
    ans = r + 1

    for i in range(N - 1):
        arr[i + 1] += arr[i]

    while l <= r:
        m = (l + r) // 2
        count = 1
        accum = m
        idx = bisect_left(arr, accum)

        while count < M:
            if idx == N:
                break
            if idx > 0:
                accum = arr[idx - 1] + m
            else:
                accum += m
            idx = bisect_left(arr, accum)
            count += 1

        if idx == N:
            ans = min(ans, m - 1)
            r = m - 1
        else:
            l = m + 1

    print(ans)