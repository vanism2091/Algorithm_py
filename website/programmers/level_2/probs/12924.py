import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""

i, i+1 -> 2*i + 1
3*i + 3
4*i + 6
연속되는 k개의 수로 표현할 수 있다 == k*i + k(k+1)/2
즉, 그 수 - k(k+1)/2 // k 하면 나누어 떨어지는 수.
이걸 
"""
from bisect import bisect_left
from math import ceil
# 숫자의 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/12924?language=python3
def solution(n):
    dp = [0] * ceil(20_000**.5)
    for i in range(1, len(dp)):
        dp[i] = i*(i+1) // 2
    answer = 0
    for i in range(1, bisect_left(dp,n)+1):
        if not (n - dp[i-1]) % i:
            answer += 1
            print(i)
    return answer

examples = [[15, 4]]

test_cases(solution, examples)

"""


(해설) num = n * m이라고 가정합시다.(n은 홀수) 이때 num이 연속된 자연수의 합으로 표현되는 방식은 다음과 같이 두 가지 방법이 있습니다. i) 중간 숫자가 m이고 연속된 n개의 자연수를 더하는 경우 : 이때 자연수의 합은 m-(n-1)/2 ~ m+(n-1)/2까지이며 이것이 올바른 합이 되려면 m-(n-1)/2 > 0. 즉 n<2m+1을 만족해야 합니다. ii) 중간 두 개의 숫자가 (n-1)/2, (n+1)/2이고 연속된 2m개의 자연수를 더하는 경우 : 이때 자연수의 합은 (n-1)/2-(m-1) ~ (n+1)/2+(m-1)이며 이것이 올바른 합이 되려면 (n-1)/2-(m-1) > 0. 즉 n > 2m-1을 만족해야 합니다. n은 홀수이므로 n < 2m+1과 n > 2m-1을 동시에 만족할 수 없고 동시에 어떤 m, n에 대해서도 두 조건 중 하나는 반드시 만족하게 됩니다. 따라서 num = n*m을 만족하는 홀수 n 하나당 연속된 자연수의 합 하나가 잘 대응되게 됩니다. 반대의 경우에는 연속된 자연수의 개수가 홀수일 때는 그 개수, 짝수일 때는 처음 수와 마지막 수의 합을 대응시키는 함수를 생각하면 연속된 자연수의 합 하나당 num = n * m을 만족시키는 홀수 n 하나가 잘 대응되는 것을 쉽게 확인할 수 있습니다. 결론적으로 num = n*m을 만족하는 홀수 n과 연속된 자연수의 합은 일대일 대응을 만족하고 그 개수가 같게 됩니다.
초항 a이고 공차 1 인 n개의 등차 수열의 합이라고 보면 Sn = n(2*a + (n-1))/2가 되는데 i) n이 홀수 이면 (2*a + (n-1)) 는 짝수 이고 ii) n이 짝수 이면 (2*a - (n-1)) 는 홀수 입니다. 쉽게 생각하면 Sn = (홀수 * 짝수)/2 인데 나누기 2때문에 짝수는 홀수가 될수도 있고 짝수가 될 수 도 있습니다. 결국, 어떤 경우든 반드시 홀수의 숫자를 포함하고 있다는 것을 확인할 수 있습니다. 따라서, n을 나눌 수 있는 홀수의 갯수와 연속된 숫자의 경우의 수가 같다고 보는것 같습니다.
위에 설명 다틀림 정확한 설명 https://gkalstn000.github.io/2021/01/21/%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84/ 직접증명해놨음

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/12924/solution_groups?language=python3
def others():
    def expressions(num):
        return len([i  for i in range(1,num+1,2) if num % i == 0])

    expressions(46)
    solution(46)


