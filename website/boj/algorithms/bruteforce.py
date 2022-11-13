import itertools

problems = [2231, 2798, 11047, 7568, 1018, 1436, 1476, 14501, 10974]
need_to_study = [1018, 1436, 1476, 14501, 10974]
need_to_solve = [ ]

def sol_2231():
    from functools import reduce
    def get_n():
        m = int(input())
        start = m - len(str(m)) * 9
        if start < 0: start = 0
        res = 0
        for i in range(start, m):
            digit_sum = reduce((lambda x, y: int(x)+int(y)), str(i))
            if m == i+int(digit_sum):
                res = i
                break
        return res
    print(get_n())
    pass
# 굳이 reduce 안써도 됨. list() map() 잘 활용하자
# max 를 쓰는 방법이 있군..!

def other_2231():
    N=int(input())
    r=0
    for i in range(max(0, N-100), N):
        if sum(map(int,list(str(i))))+i==N:
            r=i
        break
    print(r)


# combination으로 3개를 뽑는다.
# 각 tuple마다 sum을 구한다.
# element-wise m을 뺀다
# 그 결과 0보다 같거나 작은 list의 인덱스를 반환한다.
def sol_2798():
    from itertools import combinations
    _, m = map(int, input().split())
    data = list(map(int, input().split()))
    a = [(a+b+c, a+b+c-m) for a, b, c in combinations(data, 3) if a+b+c-m <= 0]
    a.sort(key=lambda t: t[1])
    print(a[-1][0])

def other_2793():
    def P(n,m,c):
        t=set()
        for i in range(n-2): # 큰 수부터 차례대로 확인 n-2번째까지 i 
            for o in range(i+1,n-1): # i 다음 수부터 n-1번째까지 o
                for p in range(o+1,n): # o 다음 수부터 n번째까지 p
                    # i, o, p는 중복되지 않음.
                    s=c[i]+c[o]+c[p]
                    if s<=m:
                        # loop돌수록 작은 수가 더해질 것이다.
                        # 따라서 s가 가장 큰 합이다
                        t.add(s)
                        break
        # set t 중 max 값이 원하는 답이다.
        return max([*t])
    print(P(*map(int,input().split()),list(sorted(map(int,input().split()))[::-1])))
    # n, m, c: 카드를 큰 수부터 내림차순 정렬
    # 오오.. 이렇게 풀 수도 있구나.. ㄷㄷ

def sol_11047():
    n, cost = map(int, input().split())
    coins = []
    for i in range(n):
        coin = int(input())
        if cost // coin == 0:
            break
        coins.append(coin)
    res = 0
    for c in reversed(coins):
        curr = cost // c
        if curr == 0:
            continue
        cost %= c
        res += curr
    print(res)


def sol_7568():
    n = int(input())
    li = []
    r = []
    for _ in range(n):
        k, h = map(int, input())
        li.append((k,h))
    for k, h in li:
        rank = 1
        for i in range(len(li)):
            tk, th = li[i]
            if tk > k and th > h:
                rank += 1
        r.append(rank)
    return " ".join(r)


# 체스판 다시 칠하기
def sol_1018():
    m, n = map(int, input().split())
    pattern = {
        0: "BWBWBWBW",
        1: "WBWBWBWB"
    }
    sq = []
    for i in range(m):
        sq.append(input())

    def check_from(x, y):
        res = 0
        for i in range(8):
            for j in range(8):
                if sq[x+i][y+j] != pattern[i%2][j]: res += 1
        return min([res, 64-res])
    res = 64
    for i in range(m-8+1):
        for j in range(n-8+1):
            curr = check_from(i, j)
            if res > curr:
                res = curr
            if res == 0: break
        if res == 0: break
    print(res)

    def other_1018():
        n, m = map(int, input().split())
        board = []

        for i in range(n):
            row = input()
            board.append([])
            for j in range(m):
                board[i].append(1 if row[j] == ('W' if (i+j)%2 == 0 else 'B') else 0)

        lst1 = []
        for i in range(n):
            lst1.append([])
            for j in range(m-7):
                lst1[i].append(sum(board[i][j:j+8]))

        lst2 = []
        for i in range(m-7):
            for j in range(n-7):
                s = 0
                for k in lst1[j:j+8]:
                    s += k[i]
                lst2.append(s)

        mx, mn = max(lst2), min(lst2)

        print(mn if mn < 64 - mx else 64 - mx)


# 영화감독 숌
def sol_1436():
    # 제일 무식한(?) 방법은 하나씩 증가시키는 것
    from itertools import count
    n = int(input())
    cnt = 0
    num = count(666)
    curr = 0
    while cnt < n:
        temp = next(num)
        if "666" in str(temp):
            curr = temp
            cnt += 1
    print(curr)


# 10000 -> 0.5~1.2sec
def sol_1436_2():
    n = int(input())

    def get_num_list(until, num_pow, num_add, s_idx):
        li = [s_idx]
        for i in range(until+1):
            if i==6:
                s_idx += (10 ** num_pow + num_add - 10 ** (num_pow-1))
            else:
                s_idx += num_add
            li.append(s_idx)
        return s_idx, [i + 1 for i in li[:-1]]
        
    def get_start_idx(num, li):
        for i, snum in enumerate(li):
            if i == len(li)-1 or num >= snum and num < li[i+1]: return i

    fo, _ = get_num_list(9, 1, 1, 0)
    fi, fi_li = get_num_list(9, 2, fo, 0)
    si, si_li = get_num_list(9, 3, fi, 0)
    _, se_li = get_num_list(2, 4, si, 0)

    cnt = 1
    res = []
    for li in [se_li, si_li, fi_li]:
        if res and res[-1] == '6':
            res.append('0')
            break
        curr_li = [cnt+(i-1) for i in li]
        idx = get_start_idx(n, curr_li)
        res.append(str(idx))
        cnt = curr_li[idx]

    num = int("".join(res)+"0665")
    curr = 0
    while cnt <= n:
        if "666" in str(num):
            curr = num
            cnt += 1
        num += 1
    print(curr)

# TODO: 분석ㄱㄱ
def other_1436():
    # O(logN) solution. 여유될 때 분석해보자.
    from bisect import bisect

    '''
        O(log(N)) solution.
        written by books1234
    '''
    def solution(N):
        # order must start at 0
        n = N - 1

        # find max digits
        f = [0, 0, 0, 1]
        D = 3
        while n >= f[D]:
            f.append(9*f[D]+9*f[D-1]+9*f[D-2]+10**(D-2))
            D += 1
        digits = [0] * (D+1)

        k = D
        count6 = 0
        lower, upper = (0, f[k])

        while k > 3 and count6 != 3:
            # partition by first digit (0~9) and 10-ary tree search
            partition = [lower+i*f[k-1] for i in range(0,7)] \
                        + [upper-(10-i)*f[k-1] for i in range(7,11)]
            digit = bisect(partition, n) - 1
            digits[k] = digit
            lower, upper = partition[digit], partition[digit+1]

            # count if current digit is 6
            count6 = count6+1 if digit == 6 else 0
            k -= 1
        
        # fill additional 6 if needed
        digits[k-(2-count6):k+1] = [6] * (3-count6)

        # string to number and add remainder
        answer = int(''.join(map(str, reversed(digits[1:])))) + n - lower
        return answer

    n = int(input().strip())
    print(solution(n))


def sol_1476():
    a, b, c = map(int, input().split())

    m, n, s = 0, 0, 0
    num = 1
    while m+1 != a or n+1 != b or s+1 != c:
        num += 1
        m = (m+1) % 15
        n = (n+1) % 28
        s = (s+1) % 19
    print(num)

# TODO: 분석ㄱㄱ
def other_1476():
    e,s,m = map(int, input().split())
    x = (6916*e+4845*s+4200*m) % 7980
    print(x if x else 7980)

def sol_14501():
    n = int(input())
    days = []
    pays = []
    for _ in range(n):
        d, p = map(int, input().split())
        days.append(d)
        pays.append(p)

    res = [0] * n
    def calc_opp_cost(from_d, to_d):
        oc = 0
        for i in range(from_d+1, to_d+1):
            pass
    for i in range(n):
        if i + days[i] > n:
            continue
        if pays[i] >= calc_opp_cost(i, i+days[i]):
            pass
        return 1 


# 순열
# permutations를 안쓰는 방법은?
def sol_10974():
    from itertools import permutations

    n = int(input())
    data = range(1, n+1)
    for t in list(permutations(data)):
        print(" ".join(map(str, t)))
    pass