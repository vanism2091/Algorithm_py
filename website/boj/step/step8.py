problems = [1978, 2581, 1929]


# 소수 찾기
# 	30840	68
def sol_1978_1():
    _ = int(input())
    num_list = list(map(int, input().split()))

    cnt = 0
    for i in num_list:
        isPrime = True
        if i == 1:
            continue
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            cnt += 1
    print(cnt)

# 	30840	68
def sol_1978_2():
    primes = [False, False] + [True] * 999
    for i in range(2, 33):
        if primes[i]:
            for j in range(i*2, len(primes), i):
                primes[j] = False
    _ = int(input())
    num_list = list(map(int, input().split()))
    n = [num for num in num_list if primes[num+1]]
    print(len(n))


# 소수 
# https://www.acmicpc.net/problem/2581
# 첫 sol:
# 속도가 640ms, 다른 분 코드에 비해 굉장히 느려서 다른 분 코드를 참고했다.
def sol_2581():
    m = int(input())
    n = int(input())
    primes = list()

    for i in range(m, n+1):
        isPrime = True
        if i == 1:
            continue
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    if not len(primes):
        print(-1)
    else:
        print(sum(primes))
        print(min(primes))

    # 다른 분 코드를 참고 후 복기한 코드
    def other_2581():
        primes = [False, False] + [True] * 9999
        for i in range(2, 101):
            if primes[i]:
                for j in range(i*2, len(primes), i):
                    primes[j] = False

        m = int(input())
        n = int(input())
        p = [i for i in range(m, n+1) if primes[i]]
        print(sum(p) if len(p) else "-1")
        print(min(p) if len(p) else "")

# 소수 구하기
# https://www.acmicpc.net/problem/2581
# 2581(소수) 다른 분 코드를 참고해서 공부 한 후
# 그걸 응용해서 클리어할 수 있었던 것 같다
# range의 두 번째 인자는 최대 자연수의 sqrt 보다 작은 최대 소수(997)+2로 잡았다
# 이것도 나는 336ms인데 다른 분은 100ms 대라, 공부가 필요할듯:)
def sol_1929():
    primes = [False, False] + [True]*(1000000-1)

    for i in range(2, 999):
        if primes[i]:
            for j in range(i*2, len(primes), i):
                primes[j] = False

    a, b = map(int, input().split())
    res = [i for i in range(a, b+1) if primes[i]]
    for num in res:
        print(num)

# 분석 필요함
    def other_1929():
        def prime(n):
            if n < 2:
                return []
            else:
                n += 1
                save = [True] * (n // 2)
                for i in range(3, int(n ** 0.5) + 1, 2):
                    if save[i // 2]:
                        k = i * i
                        save[k // 2::i] = [False] * ((n - k - 1) // (2 * i) + 1)
            return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]

        from bisect import bisect_left as bl
        m, n = map(int, input().split())
        s = prime(n)
        print(*s[bl(s, m):])