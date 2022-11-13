
"""

"""
# 통계학
# https://www.acmicpc.net/problem/2108
def sol_2108():
    import sys
    p = sys.stdin.readline
    N = int(input())
    nums = list(map(int, sys.stdin.read().splitlines()))
    # nums = [int(p()) for _ in range(N)]
    res = [0] * 8001
    def get_idx(n): return n if n >= 0 else abs(n)+4000
    def get_num(i): return i if i <= 4000 else -(i-4000)
    for num in nums:
        res[get_idx(num)] += 1

    res = [(get_num(i), v) for i, v in enumerate(res) if v]
    res.sort()

    total_sum = 0
    for num, v in res:
        total_sum += (num * v)
    print(round(total_sum/N))

    m_th = N//2
    if m_th:
        m_val, temp = -4001, 0
        for num, v in res:
            temp += v
            if temp > m_th:
                m_val = num
                break
        print(m_val)
    else: 
        print(nums[0])

    freq_times = max([v for num, v in res])
    freq_nums = [num for num, v in res if v == freq_times]
    if len(freq_nums) == 1:
        print(freq_nums[0])
    else:
        print(freq_nums[1])

    print(res[-1][0] - res[0][0])


if __name__ == "__main__":
    print(sol_2108())

"""

"""
# https://www.acmicpc.net/problem/status/2108/1003/1
def other_2108():
    pass



