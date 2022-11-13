# TODO: 타인 코드 확인 ㄱ
# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
# 88 / 52 한 번 확인 ㄱㄱ
def sol_2775():
    n = int(input())
    for i in range(n):
        k = int(input())
        n = int(input())
        res = [[col for col in range(1, n+1)] for row in range(k+1)]
        for j in range(1, k+1):
            # j = 1 ... k 층
            for l in range(1, n+1):
                res[j][l-1] = sum(res[j-1][:l])
        print(res[k][n-1])
        
# 설탕 배달
# 30840	72
# https://www.acmicpc.net/problem/2839
def sol_2839():
    n = int(input())
    def isPossible(n):
        div = n // 5
        rem = n  % 5
        for i in range(div+1):
            if rem % 3 == 0:
                return div+rem//3
            else:
                div -= 1
                rem += 5
        return -1

    print(isPossible(n))


# 큰 수 A+B
# python is GOD!
# https://www.acmicpc.net/problem/10757
def sol_10757():
    a, b  = map(int, input().split())
    print(a+b)