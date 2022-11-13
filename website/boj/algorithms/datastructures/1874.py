
"""
1. 1부터 n까지
2. n개의 줄에 -> 입력을 read().splitlines()로 받자
3. 첫 번째 숫자와 같은 숫자가 나올 때 까지 push함
    3.1 처음에는, 첫 숫자를 확인하고 첫 숫자만큼 push, 
        orig list= orig.popleft()
        working_list = [range(1, f_n+1)]
        worked = ['+'] * f_n
    curr = orig_list.pop_left()
    3.2 if curr == working_list[-1]:
            # pop
            working_list.pop()
            worked.append('-')
        elif: curr < working_list[-1]
            return NO
        else:
            # push
            
"""
# 스택 수열
# https://www.acmicpc.net/problem/1874
def sol_1874(N, nums):
    from sys import stdin
    from collections import deque
    # inputs = stdin.read().splitlines()
    # N = int(inputs[0])
    # oq = deque(map(int,inputs[1:N+1]))
    # [4, 3, 6, 8, 7, 5, 2, 1]
    # 1 2 5 3 4
    oq = deque(nums)
    working_list = []
    worked = []
    push_queue = 1
    while oq:
        curr = oq.popleft()
        if curr == push_queue:
            worked.extend(['+', '-'])
            push_queue += 1
            continue
        if working_list:
            if curr == working_list[-1]:
                working_list.pop()
                worked.append('-')
            elif curr < working_list[-1]:
                return 'NO'
            else:
                # push
                working_list.extend(range(push_queue, curr))
                worked.extend(['+']*(curr-push_queue+1)+['-'])
                push_queue = curr+1
        else:
            working_list.extend(range(push_queue, curr))
            worked.extend(['+']*(curr-push_queue+1)+['-'])
            push_queue = curr+1
    return '\n'.join(worked)

sol_1874(8, [4, 3, 6, 8, 7, 5, 2, 1])
# print(sol_1874(5, [1, 2, 5, 3, 4]))

# if __name__ == "__main__":
#     print(sol_1874())

"""

"""
# https://www.acmicpc.net/problem/status/1874/1003/1
def other_1874():
    pass



