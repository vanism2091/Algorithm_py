
# 수 찾기
# 46800	480
# https://www.acmicpc.net/problem/1920
def sol_1920():
    import sys
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    querys = list(map(int, input().split()))

    # 정렬 후에
    nums.sort()

    # binary search로 존재 여부 확인
    def is_exist(array, target):
        start = 0
        end = len(array)-1
        while start <= end:
            mid = (start+end)//2
            if array[mid] > target:
                end = mid - 1
            elif array[mid] < target:
                start = mid + 1
            else:
                return True
        return False
    
    print("\n".join(["1" if is_exist(nums, target) else "0" for target in querys]))

import sys
from bisect import bisect_right, bisect_left

# 다른 방식으로 한 번만 풀어보자
# input을 더 간단하게 받을 방법이 있을까?
# sort 한 후, bisect_left, bisect_right를 돌린다. 
# 둘의 값이 같으면(존재x) 0, 다르면(존재) 1
# 48884	264   (이전, 46800	480)
# 오오오 줄었음..!
def sol_1920():
    input = sys.stdin.readline
    N = int(input())
    numbers = list(map(int, input().split()))
    M = int(input())
    querys = list(map(int, input().split()))

    numbers.sort()

    return "".join(["1\n" if in_list(numbers, query) else "0\n" for query in querys])

def in_list(li, query):
    return True if bisect_right(li, query) == bisect_left(li, query) else False
    

if __name__ == '__main__':
    print(sol_1920())

"""
ㅋㅋㅋㅋ아니 뭔가 허무한데
numbers를 Set에 넣고
a안에 query 받을 때마다 존재 체크ㅋㅋㅋㅋ
너무 어렵게 생각하지 말자 :):):)
"""
# https://www.acmicpc.net/problem/status/1920/1003/1
def other_1920():
    import sys
    input=sys.stdin.readline
    def sol():
        input()
        a=set(input().split())
        input()
        print('\n'.join(('1' if i in a else '0' for i in input().split())))
    sol()



