
"""
최대 600_000글까지 입력 가능
input:
    1. 문자열 (길이 N [1, 100_000])
    2. 명령어 개수 M [1, 500_000]
    3~M+2. 입력할 명령어
명령어는 L, D, B, P $
    L: 커서를 왼쪽으로 한 칸 옮김 (커서가 맨 앞이면 무시)
    D: 커서를 오른쪽으로 한 칸 옮김 (커서 맨 뒤면 무시)
    B: 커서 왼쪽의 문자를 삭제함 (커서가 맨 앞이면 무시)
        삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것 처럼 나타나지만,
        커서 오른쪽에 있던 문자는 그대로임
    P $ : $라는 문자를 커서 왼쪽에 추가함
최초 커서는 문장의 맨 뒤에 위치하고 있다.
출력 : 모든 명령 수행 후 편집기에 입력되어 있는 문자열

음.. 문자열을 리스트로 만든 후에
idx로 커서를 추적,
    L: idx - 1 if idx > 0 else idx
    D: idx + 1 if idx < N else idx
    B: if idx > 0:
            # 삭제할 것은 words[idx-1]
            words = words[:idx-1] + words[idx:]
            idx -= 1
    P $: 
        words = (words[:idx] if idx>0 else []) + ["$"] + words[idx:]
        idx += 1

위 코드로 했는데 PyPy3으로 해도 시간초과 떴다.
list 말고 다른 자료 구조를 사용해야 한다.
list를 한다면, 이 코드 대로면
100_000 * 500_000 = 5*1e10 :) 잘못했습니다
1e7안으로 줄여야 한다. 
연결리스트로 삽입과 삭제 시 걸리는 시간을 줄이자. 
연결리스트는 파이썬의 경우 특별한 모듈이 있지 않고 직접 구현해야 한다.
"""
# 에디터
# https://www.acmicpc.net/problem/1406
def sol_1406():
    class Char:
        def __init__(self, val=0, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev
    from sys import stdin
    inputs = stdin.read().splitlines()

    words = Char("S") # start node
    curr = words
    for c in inputs[0].rstrip():
        curr.next = Char(c, prev=curr)
        curr = curr.next

    for i in range(int(inputs[1])):
        curr_command = inputs[2+i]
        if curr_command[0] == 'L':
            if curr.val != "S":
                curr = curr.prev
        elif curr_command[0] == 'D':
            if curr.next != None:
                curr = curr.next
        elif curr_command[0] == "B":
            if curr.val != "S":
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr = curr.prev
        else:
            new_char = Char(curr_command[2], prev=curr)
            new_char.next = curr.next
            if curr.next != None:
                curr.next.prev = new_char
            curr = new_char
    char = words
    while char.next != None:
        print(char.next, end="")
        char = char.next
    # return "".join(words)

# Python    165252	1604
def sol_1406():
    class Char:
        def __init__(self, val=0, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev
            
    from sys import stdin
    inputs = stdin.read().splitlines()

    words = Char("S") # start node
    curr = words
    for c in inputs[0].rstrip():
        curr.next = Char(c, prev=curr)
        curr = curr.next

    for i in range(int(inputs[1])):
        curr_command = inputs[2+i]
        if curr_command[0] == 'L':
            if curr.val != "S":
                curr = curr.prev
        elif curr_command[0] == 'D':
            if curr.next != None:
                curr = curr.next
        elif curr_command[0] == "B":
            if curr.val != "S":
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                curr = curr.prev
        else:
            curr.next = Char(curr_command[2], next=curr.next, prev=curr)
            if curr.next.next != None:
                curr.next.next.prev = curr.next
            curr = curr.next
    char = words
    while char.next:
        print(char.next.val, end="")
        char = char.next

if __name__ == "__main__":
    print(sol_1406())

"""
커서를 기준으로 list를 좌 우로 나눔
txt_l 커서 txt_r
L일 때는 l에서 빼서 r에 넣고
D일 때는 r에서 빼서 l에 넣고
B일때는 l에서 pop,
P일때는 l에 append($)
wow...:)
"""
# https://www.acmicpc.net/problem/status/1406/1003/1
def other_1406():
    from sys import stdin
    l = stdin.read().rstrip().split("\n")
    txt_l = list(l[0])
    txt_r = []
    l = l[2:]

    for o in l:
        if o[0] == "P":
            txt_l.append(o[2])
        elif o=="L" and txt_l:
                txt_r.append(txt_l.pop())
        elif o=="D" and txt_r:
                txt_l.append(txt_r.pop())
        elif o=="B" and txt_l:
                txt_l.pop()

    print("".join(txt_l)+"".join(txt_r[::-1]))



