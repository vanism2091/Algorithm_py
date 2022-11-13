# 단계별로 풀어보기 - 9_재귀
# https://www.acmicpc.net/step/19

# 팩토리얼
# https://www.acmicpc.net/problem/10872
def sol_10872():
    n = int(input())
    def factorial(n):
        if n == 1 or n == 0:
            return 1
        else:
            return n  * factorial(n-1)
    print(factorial(n))

# 피보나치 수 5
def sol_10870():
    n = int(input())
    def fibo(n):
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            return fibo(n-1)+fibo(n-2)
    print(fibo(n))

# 재귀함수가 뭔가요?
def sol_17478():
    target = int(input())
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    def answer(n):
        if n==target:
            print("____"*n+'"재귀함수가 뭔가요?"')
            print("____"*n+'"재귀함수는 자기 자신을 호출하는 함수라네"')
            print("____"*n+'라고 답변하였지.')
        else:
            print("____"*n+'"재귀함수가 뭔가요?"')
            print("____"*n+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
            print("____"*n+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
            print("____"*n+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
            answer(n+1)
            print("____"*n+'라고 답변하였지.')
        
    answer(0)

# 별 찍기 - 10
def sol_2447():
    pass

# 하노이의 탑 이동 순서
def sol_hanoi():
    # 20 일 때 패스 못함. 더 빠른 방법을 생각해보자
    target = int(input())
    move_cnt = 0
    res = ""
    hanoi_res = {}

    def hanoi(n, f, t):
        global move_cnt
        global res
        if n == 1:
            move_cnt += 1
            res += f'{f} {t}\n'
        else:
            hanoi(n-1, f, 6-(f+t))
            move_cnt += 1
            res += f'{f} {t}\n'
            hanoi(n-1, 6-(f+t), t)

    hanoi(target, 1, 3)
    print(move_cnt)
    print(res.rstrip())