
import collections
import itertools
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
1차 시도 결과
테스트 1~6 〉	통과

테스트 7 〉	실패 (0.13ms, 10.4MB)

테스트 8~12 〉	통과

테스트 13 〉	실패 (0.11ms, 10.4MB)

테스트 14~17 〉	통과

테스트 18 〉	실패 (0.10ms, 10.4MB)
테스트 19 〉	실패 (0.08ms, 10.3MB)

테스트 20 〉	통과

테스트 21 〉	실패 (0.50ms, 10.5MB)
테스트 22 〉	실패 (0.24ms, 10.3MB)

테스트 23 〉	통과

테스트 24 〉	실패 (0.32ms, 10.5MB)

채점 결과
정확성: 62.5
합계: 62.5 / 100.0

1. 런타임에러
생각해보니 capa가 1이면 [-2] 조회할 때 오류남.. 이거 수정하니 런타임 에러는 사라짐.
    합계: 70.8 / 100.0
2. 실패
아니... 하.... 시간 비교 로직을 잘못 세움... 정신차려어
before
    return ch <= self.hour and cm <= self.minute
after    
    return ch < self.hour or (ch == self.hour and cm <= self.minute)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""
# [1차] 셔틀버스
# https://school.programmers.co.kr/learn/courses/30/lessons/17678?language=python3

class Bus:
    def __init__(self, times, interval, capacity):
        self.times = times
        self.interval = interval
        self.capacity = capacity
        self.seat_left = capacity
        self.hour = 9
        self.minute = 0
    
    def departure(self):
        self.times -= 1
        carry, self.minute = divmod(self.minute + self.interval, 60)
        self.hour += carry

    def can_carry(self, crew):
        ch, cm = map(int, crew.split(':'))
        return ch < self.hour or (ch == self.hour and cm <= self.minute)

    def get_departure_time(self):
        return f"{self.hour:02}:{self.minute:02}"

    def count_carry(self, crews):
        return len([crew for crew in crews if self.get_departure_time() >= crew])

        

def solution(n, t, m, timetable):
    bus = Bus(n, t, m)
    crews = collections.deque(sorted(timetable))
    while bus.times > 1:
        seat_left = m
        while seat_left > 0:
        # while seat_left > 0 and crews:
            crew = crews.popleft()
            if bus.can_carry(crew):
                seat_left -= 1
            else:
                crews.appendleft(crew)
                break
        # 버스가 떠남. 버스 정보 업데이트
        bus.departure()
    # 막차인 경우
    candis = list(itertools.islice(crews, bus.capacity))
    if bus.capacity > bus.count_carry(candis):
        return bus.get_departure_time()
    else:
        return one_minute_prev(candis[-1])

def one_minute_prev(crew):
    ch, cm = map(int,crew.split(':'))
    return f'{ch-1:02}:59' if cm == 0 else f'{crew[:3]}{cm-1:02}'
    

# examples = [[1, 1, 5, ['08:00', '08:01', '08:02', '08:03'], '09:00'], [2, 10, 2, ['09:10', '09:09', '08:00'], '09:09'], [2, 1, 2, ['09:00', '09:00', '09:00', '09:00'], '08:59'], [1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01'], '00:00'], [1, 1, 1, ['23:59'], '09:00'], [10, 60, 45, ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59'], '18:00']]
examples = [[10, 25, 1, ["09:00", "09:10" ,"09:20" ,"09:30" ,"09:40" ,"09:50",
"10:00", "10:10" ,"10:20" ,"10:30" ,"10:40" ,"10:50"], '10:29']]
test_cases(solution, examples)


"""

"""
# https://school.programmers.co.kr/learn/courses/30/lessons/17678/solution_groups?language=python3
def others():
    pass


