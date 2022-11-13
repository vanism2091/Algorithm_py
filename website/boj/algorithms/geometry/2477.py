
"""
짝수번째, 홀수번째 따로 나눠서 배열로 담음.
max끼리 곱하고, min끼리 곱한 후 전자에서 후자를 빼면 밭의 넓이가 나옴.
ㄴㄴ 이 풀이가 문제의 예시에는 유효하겟지만, 역ㄱ자일때는 유효하지 않음.

"""
# 참외밭
# https://www.acmicpc.net/problem/2477
def sol_2477():
    import sys
    inputs = sys.stdin.read().splitlines()
    num_melon = int(inputs[0])
    total = [int(inputs[i].split()[1]) for i in range(1,7)]
    one_side_max_idx = total.index(max([total[t] for t in range(1,7,2)]))
    other_side_max_idx = total.index(max([total[t] for t in range(2,7,2)]))
    def is_former_latter(f_idx, la_idx): return (idx + 6) % 6
    if 
    # if
    # big_area = max(one_side) * max(other_side)
    # small_area = min(one_side) * min(other_side)
    # return num_melon * (big_area - small_area)

print(sol_2477())
# if __name__ == "__main__":

"""

"""
# https://www.acmicpc.net/problem/status/2477/1003/1
def other_2477():
    pass
