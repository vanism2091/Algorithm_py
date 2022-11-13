import sys
import os 
sys.path.insert(0, os.getcwd() +'/python')

import make_python_file as m
problems = [11399, 1764, 2751, 1931, 2108, 2217, 1946, 11004, 11651, 10815]
need_to_solve = [1946, 10815]
need_to_study = [2751, 1931, 2217, 11004, 11651]
new_problems = [1181]
m.make_template(os.path.abspath(__file__), problems=new_problems)


# ATM
# https://www.acmicpc.net/problem/11399
# 다른 분 코드와의 비교
#   - (for문 이후) 리스트 내 연산보다 숫자 연산이 더 빠르고
#   - 메모리 상으로도 이득될 게 없음.
#   - 두 가지가 모두 가능한 경우에는, 
#   - 리스트 내 값을 변경하기 보다 새 변수를 만들어서 답을 만들자
# 30840	68
def sol_11399():
    n = int(input())
    li = list(map(int,input().split()))

    li.sort() # O(NlogN)
    for i in range(n): # O(N)
        li[i] *= n-i 
    print(sum(li)) # O(N)

# 29284	52
def other_11399():
    a = int(input())
    l = []
    total = 0
    cur = 0
    l = list(map(int, input().split()))

    l.sort()
    for x in l:
        cur += x
        total += cur
    print(total)
    pass


# 듣보잡
# https://www.acmicpc.net/problem/1764
# 42108	124
def sol_1764():
    import sys
    p = sys.stdin.readline
    n, m = map(int, input().split())
    a = set()
    b = set()
    for _ in range(n):
        a.add(p().rstrip())
    for _ in range(m):
        b.add(p().rstrip())
    a = list(a & b)
    a.sort()
    print(len(a))
    for i in a:
        print(i)
    pass

# sys.stdin.read().splitlines()로 긴 names를 한꺼번에 받아오기
# 41136	84
def other_1764():
    import sys
    n, m = map(int, input().split())
    nameList = sys.stdin.read().splitlines()
    hearset = set(nameList[:n])
    seeset = set(nameList[n:])
    ret = list(hearset & seeset)
    ret.sort()
    print(len(ret))
    for i in ret:
        print(i)



# 수 정렬하기
# N 이 1000000 일때 nlogn을 계산했더니 2천만에 육박.. 시간 제한은 2초
# 입력 받을 때부터 첫 번째 수를 피봇으로 잡아 두 개로 나눠볼까.
# https://www.acmicpc.net/problem/2751

# TODO: 다른 사람 코드 확인해보기

# Python3:  86464   1660
# PyPy3 :   212888	784
def sol_2751():
    import sys
    p = sys.stdin.readline
    n = int(input())
    pivot = int(p())
    l, r = [], []
    for _ in range(n-1):
        c = int(p())
        if pivot >= c:
            l.append(c)
        else:
            r.append(c)
    l.sort()
    r.sort()
    for i in l+[pivot]+r:
        print(i)
        
    
    pass
# pypy3로 452ms...
def other_2751():
    from sys import stdin, stdout
    input()
    arr = sorted(list(map(int, stdin.read().split())))
    stdout.write('\n'.join(map(str,arr)))
    pass


# TODO: 1. 성공은 했지만 조금만 더 손 보면 더 좋은 구조로 코딩할 수 있을 것 같은데,
#           생각해보기
#       2. 그 후 다른 분 코드 살펴보기
# 회의실 배정
# https://www.acmicpc.net/problem/1931
# 43908	268
def sol_1931():
    import sys
    p = sys.stdin.readline
    n = int(input())
    li = [tuple(map(int, p().split())) for _ in range(n)]
    li.sort()
    cnt = 0
    b = 0
    for i in range(len(li)):
        if i == n-1:
            if b <= li[i][0]:
                cnt += 1
            break
        if li[i][1] > li[i+1][1]:
            continue
        if b > li[i][1]:
            b = li[i][1]
        elif b <= li[i][0]:
            cnt += 1
            b = li[i][1]
    print(cnt)
    pass

# 43644	184
def other_1931():
    from sys import stdin
    def solve():
        n=int(stdin.readline().rstrip())
        dic={}
        trash=0
        ltrash={}
        for i in range(n):
            a,b=map(int,stdin.readline().split())
            if a not in dic and b!=a: dic[a]=b
            elif b==a:
                trash+=1
                if b not in ltrash: ltrash[b]=0
            elif dic[a]>b and b!=a: dic[a]=b 
        for e in ltrash:
            if e not in dic:
                dic[e]=e
                trash-=1
        arr=list(dic)
        arr.sort()
        tmp=dic[arr[0]]
        cnt=1
        for i in range(1,len(arr)):
            if tmp>dic[arr[i]]:
                tmp=dic[arr[i]]
            else:
                if arr[i]>=tmp:
                    cnt+=1
                    tmp=dic[arr[i]]
        print(cnt+trash)
    solve()
    pass





# 통계학
# read().splitlines() 써보기 좋을 문제인듯
# 4000을 넘지 않는데 500,000개의 입력이면.. 
# counting sort 해봐도 괜찮을듯?
# 아.. 정수의 절댓값이:).. 음수가 나올수 있다..:)
# 카운팅소트 하면 O(5십만 + 8001)임 일단 못먹어도 고
# Num: 0 / -1 1 / -2 2 / -3, 3 / ...
# Idx: 0 / 1, 2 / 3, 4 / 5, 6 / ... 
# https://www.acmicpc.net/problem/2108
def sol_2108():
    import sys
    n = int(input())
    nums = list(map(int, sys.stdin.read().splitlines()))
    res = [0] * 8001
    def get_idx(n): return 2*n if n>=0 else 2*abs(n)-1
    def get_num(i): return i//2 if i%2 == 0 else -(i//2+1)
    for num in nums:
        res[get_idx(num)] += 1

    # 산술평균
    total_sum = 0
    for i in range(len(res)):
        total_sum += get_num(i) * res[i]
    print(int(round(total_sum/n,0)))

    # 중앙값
    m_th = n//2
    temp = 0
    # 7999, 7997, ..., 1, 0, 2, 4, ... 8000
    for i in [*range(7999, 0, -2), 0, *range(2, 8001, 2)]:
        # if min_idx == -1 and res[i] != 0:
        #     min_idx = i
        if temp >= m_th:
            temp = i
            break
        temp += res[i]
    print(get_num(temp))

    # 최빈값
    freq_times = max(res)
    idxs = [-idx if idx%2 else idx  for idx, v in enumerate(res) if v == freq_times]
    if len(idxs) == 1:
        print(get_num(abs(idxs[0])))
    else:
        idxs.sort()
        print(get_num(abs(idxs[1])))

    # 범위
    for i in [*range(7999, 0, -2), 0, *range(2, 8001, 2)]:
        if res[i] != 0:
            min_idx = i
            break
    for i in range(*range(8001, 1, -2), 0, *range(1, 8000, 2)):
        if res[i]:
            max_idx = i
            break
    print(get_num(max_idx)-get_num(min_idx))
    pass

# 풀다가 생각해낸, 중간에 res를 그냥 v가 있는 것만 남기고 소트미리하면 좋을 듯 :)
# 근데 왜 틀리는 건지.. 예외 케이스.. 뭘까.. 생각하기 싫다.. 흑흑
def sol_2_2108():
    import sys
    p = sys.stdin.readline
    n = int(input())
    # nums = list(map(int, sys.stdin.read().splitlines()))
    nums = [int(p()) for _ in range(n)]
    res = [0] * 8001
    def get_idx(n): return 2*n if n>=0 else 2*abs(n)-1
    def get_num(i): return i//2 if i%2 == 0 else -(i//2+1)
    for num in nums:
        res[get_idx(num)] += 1

    res = [(get_num(i), v) for i, v in enumerate(res) if v]
    res.sort()

    total_sum = 0
    for n, v in res:
        total_sum += num * v
    print(int(round(total_sum/n,0)))

    m_th = n//2
    if m_th:
        temp = 0
        for n, v in res:
            if temp >= m_th:
                temp = n
                break
            temp += v
        print(temp)
    else: 
        print(nums[0])

    freq_times = max([v for n, v in res])
    freq_nums = [n for n, v in res if v == freq_times]
    if len(freq_nums) == 1:
        print(freq_nums[0])
    else:
        print(freq_nums[1])

    print(res[-1][0] - res[0][0])

def other_2108():
    # 반례 찾다가 흥미로운 C언어 풀이가 있어서 가져와봤음
    #include <stdio.h>
    # #include <algorithm>

    # int main(){
    #     double cnt=0;
    #     int n;
    #     scanf("%d",&n);
    #     int arr[n],key[10000]={0};
    #     for(int i=0;i<n;i++){
    #         scanf("%d",arr+i);
    #         cnt+=arr[i];
    #         key[arr[i]+4000]++;
    #     }
    #     int be[2]={0},now[2]={0};
    #     for(int i=8010;i>=0;i--){
    #         if(key[i]>=now[0]){
    #             be[0]=now[0];
    #             be[1]=now[1];
    #             now[0]=key[i];
    #             now[1]=i;
    #         }
    #     }
    #     std::sort(arr,arr+n);
    #     printf("%0.lf\n",cnt/5);
    #     printf("%d\n",arr[n/2]);
    #     if(be[0]==now[0]){
    #         printf("%d\n",be[1]-4000);
    #     }
    #     else{
    #         printf("%d\n",now[1]-4000);
    #     }
    #     printf("%d",arr[n-1]-arr[0]);
    #     return 0;
    # }

    pass





# 내림차순으로 정렬한 후,
# idx+1 * val 리스트 만든 후
# 최대 값을 출력하면 됨
# 안되면 카운팅소트 ㄱ
# 해결! 시간 날 때 카운팅 소트도 구현해보자
# TODO: 1. 카운팅 소트 구현해보기       
#       2. 다른 분 코드 분석
# https://www.acmicpc.net/problem/2217
# 	42132	120
def sol_2217():
    import sys
    N = int(input())
    ropes = list(map(int, sys.stdin.read().splitlines()))
    ropes.sort(reverse=True) #O(NlogN)
    ropes = [(i+1)*val for i, val in ropes] # O(N) 
    print(max(ropes))   # O(N)
    pass

# 	29056	92
def other_2217():
    import sys
    In = sys.stdin.readline

    def main():
        n = int(In())
        rope = [0] * 10001
        for _ in range(n):
            rope[int(In())] += 1
        m, s = 0, 0
        for x in range(10000,-1,-1):
            s += rope[x]
            m = max(m, x * s)
        print(m)
    main()
    pass





# 각 테스트 케이스 별로 우선 오름차순으로 소팅 후에
# 위부터 s[1] 보다 작은 i+1:n까지의 지원자를 쳐냄
# 그걸 n-1까지 함
# 시간 초과
# https://www.acmicpc.net/problem/1946
def sol_1946():
    import sys
    from collections import deque
    p = sys.stdin.readline
    T = int(p())
    for _ in range(T):
        N = int(p())
        scores = [tuple(map(int,p().split())) for _ in range(N)]
        scores.sort()

        res = 0
        q = deque([s for _, s in scores])
        while q :
            curr = q.popleft()
            res += 1
            q = deque([s for s in q if s < curr])
        print(res)
        
        
        
        
    pass

def other_1946():
    pass



# TODO: need to study 다른 분 코드
# 느낀 점
# 확실히 pypy3이 시간 덜걸리는구나.. 너무 오래걸리면 그걸로도 제출해봐야겠다.
# 그냥 sort 돌리고 K번째 수 프린트해도 되나..? 일단 해봐
# 오름차순 정렬했을 때 앞에서 K 번째 수..
# https://www.acmicpc.net/problem/11004
# Python : 	622588	3984
# PyPy3 :   646904	2648
def sol_11004():
    import sys
    p = sys.stdin.readline
    N, K = int(p().split())
    nums = list(map(int, p().split()))
    nums.sort()
    print(nums[K-1])
    pass

# PyPy3 :	712324	2376
def other_11004():
    from random import randint
    import sys
    input = sys.stdin.readline

    def partition(a, s, e):
        i = s
        for j in range(s, e):
            if a[j] <= a[e]:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[e] = a[e], a[i]
        return i

    def isone(a, s, e):
        for i in range(s, e):
            if a[i] != a[e]:
                return False
        return True

    def selection(a, s, e, i):
        if s == e or isone(a, s, e):
            return a[s]
        p = randint(s, e)
        a[p], a[e] = a[e], a[p]
        q = partition(a, s, e)
        diff = q-s+1
        if i < diff:
            return selection(a, s, q-1, i)
        elif i == diff:
            return a[q]
        else:
            return selection(a, q+1, e, i-diff)

    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    print(selection(a, 0, n-1, k))



# TODO: 다른 분 코드와 비교 및 공부
# 인풋을 튜플 리스트로 바꾸고
# 0에 대해 sort한 후
# 다시 1에 대해 sort
# nlogn * 2, 점은 100,000개.. 200만 *2 ? 파이썬 2천번이니까 ㄱㅊ겟징
# 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651
# 46256	372
def sol_11651():
    import sys
    N = int(input())
    coords = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    coords.sort()
    for i, j in sorted(coords, key=lambda x: x[1]):
        print(i, j)

# 1, 2 stdin, stdout: stdin은 자주 봤는데 stdout은 덜 친숙하다.
# TODO: 각잡고 둘에 대해서 공부해보자. 
# 3: sys.stdin.readlines() 만 써도 속도가 훨씬 빨라진다.

# 44136	180
def other_11651_1():
    from sys import stdin, stdout
    def key(i):
        x,y=i.split()
        return int(x)/1000000+int(y)
    i=stdin.readlines()[1:]
    stdout.write(''.join(sorted(i, key=lambda x:key(x))))
    pass
# 43352	184
def other_11651_2():
    import sys
    def thres(e):
        x, y = e.split()
        return int(x)/1000000 + int(y)
    input = sys.stdin.readline
    print = sys.stdout.write
    l = sys.stdin.readlines()[1:]
    l = sorted(l, key=lambda x: thres(x))
    print(''.join(l))
    pass
	# 41640	204
def other_11651_3():
    import sys
    lst = sys.stdin.readlines()[1:]
    lst.sort(key=lambda x: int(x.split()[0]))
    lst.sort(key=lambda x: int(x.split()[1]))
    print(''.join(lst))



# TODO: unsolved
# 두 배열 각각 sort 한 후 
# index 요리조리하며 없으면 0 있으면 1
# 숫자 카드
# https://www.acmicpc.net/problem/10815
def sol_10815():
    import sys
    p = sys.stdin.readline
    N = int(p())
    cards = list(map(int, p().split()))
    M = int(p())
    test_cases = list(map(int, p().split()))
    cards.sort()
    test_cases.sort()
    j = 0
    for card in cards:
        pass
    pass

# 뭐지...? 이게 내 풀이...?
# in을 위해 set을 썼구나 :)
from sys import stdin
inputs = stdin.read().splitlines()

def sol_10815():
    num = set(map(int, inputs[1].split()))
    return " ".join(["1" if n in num else "0" for n in map(int,inputs[3].split())])
                     
# if __name__ == "__main__":
print(sol_10815())

def other_10815():
    pass





# 
# https://www.acmicpc.net/problem/1181
# sol1: 37500	92
# sol1: 35452	88
# 처음에 출력형식이 문제가 있었다.
# readlines 의 output list에는 단어 끝에 \n이 붙어있다.
# 그래서 map, rstrip을 돌렸다. "str.rstrip"
# 다시 생각해보니 그냥 다 join후 마지막에 rstrip을 하면 될 것 같았고, 미미하지만 속도 증가함.
def sol_1181():
    import sys
    words = list(set(map(str.rstrip, sys.stdin.readlines()[1:])))
    words.sort()
    print("\n".join(sorted(words, key=lambda x: len(x))))
    pass
def sol_1181_2():
    pass

#	32644	80
def other_1181():
    import sys
    word=set()
    for i in range(int(input())):
        word.add(sys.stdin.readline().rstrip())
        word=list(word)
        word.sort()
        word.sort(key=lambda x:len(x))
        print("\n".join(word))
    pass



