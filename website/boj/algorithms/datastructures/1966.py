
"""

"""
# 프린터 큐
# https://www.acmicpc.net/problem/1966
def sol_1966():
    from sys import stdin
    from collections import deque
    inputs = stdin.read().splitlines()
    for i in range(int(inputs[0])):
        N, loc = map(int, inputs[2*i+1].split())
        if N == 1:
            print(1)
            continue
        docs = deque([(p, i) for i, p in enumerate(map(int, inputs[2*i+2].split()))])
        curr_max = max(docs)[0]
        cnt = 0
        while docs:
            curr_doc = docs.popleft()
            if curr_doc[0] == curr_max:
                cnt += 1
                if docs:
                    curr_max = max(docs)[0]
                if curr_doc[1] == loc:
                    print(cnt)
                    break
            else:
                docs.append(curr_doc)


sol_1966()
if __name__ == "__main__":
    print(sol_1966())

"""

"""
# https://www.acmicpc.net/problem/status/1966/1003/1
def other_1966():
    pass



