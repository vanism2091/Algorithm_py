
"""
# 잃어버린 괄호
# 식을 하나씩 순회하다가 '-'를 만났을 때, 
# 괄호를 이전에 열었다면 닫고 - 뒤에 열고, 
# 안열었다면 - 뒤에 열고
# eval() 사용
"""
# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
def sol_1541():
    exp = input()
    res = []
    is_open = False
    is_leading = True
    for c in exp:
        if c == '-':
            if is_open:
                res.append(")")
            res.append(c)
            res.append("(")
            is_open = True
            is_leading = True
        elif c == '+':
            is_leading = True
            res.append(c)
        else:
            if not is_leading or c != '0':
                res.append(c)
                is_leading = False
    if is_open:
        res.append(")")
    print(eval("".join(res)))
    # 처음에 런타임에러났는데, 0으로 시작하는 숫자가 eval에 들어가서 oct 취급되었기 때문.


if __name__ == "__main__":
    print(sol_1541())

"""

"""
# https://www.acmicpc.net/problem/status/1541/1003/1
def other_1541():
    e = [sum(map(int, x.split('+'))) for x in input().split('-')]
    print(e[0]-sum(e[1:]))



