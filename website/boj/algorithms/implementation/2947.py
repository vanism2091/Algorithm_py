
"""

"""
# 나무 조각
# 30840	76
# https://www.acmicpc.net/problem/2947
def sol_2947():
    import sys
    arr = list(map(int, sys.stdin.readline().split()))
    while arr != [1, 2, 3, 4, 5]:
        for i in range(4):
            if arr[i] <= arr[i+1]:
                continue
            arr[i], arr[i+1] = arr[i+1], arr[i]
            # print(" ".join(map(str,arr)))
            print(*arr)


if __name__ == "__main__":
    sol_2947()

"""

"""
# https://www.acmicpc.net/problem/status/2947/1003/1
def other_2947():
    pass



