
"""

"""
# 문자열
# https://www.acmicpc.net/problem/1120
def sol_1120():
    a, b = input().split()

    min_val = 51
    len_a = len(a)
    for i in range(len(b)-len_a+1):
        temp = 0
        for ac, bc in zip(a, b[i:i+len_a]):
            if ac!=bc:
                temp += 1
        min_val = min(min_val, temp)
    print(min_val)
        


if __name__ == "__main__":
    print(sol_1120())

"""

"""
# https://www.acmicpc.net/problem/status/1120/1003/1
def other_1120():
    pass



