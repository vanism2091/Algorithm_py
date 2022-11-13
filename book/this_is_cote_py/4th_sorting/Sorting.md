
TODO: 머지소트 고민 후, 현재 파이썬 기본 라이브러리에서 소팅 어떻게 구현되어 있을지 고민 후 알아보기!

- [정렬, 나만의 요약](#정렬-나만의-요약)
  - [네 가지 정렬 알고리즘 간단 비교](#네-가지-정렬-알고리즘-간단-비교)
- [들어가며](#들어가며)
- [선택 정렬](#선택-정렬)
- [삽입 정렬](#삽입-정렬)
- [퀵 정렬](#퀵-정렬)
- [계수 정렬 (카운팅 정렬)](#계수-정렬-카운팅-정렬)


## 정렬, 나만의 요약

- 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장하도록 설계되어 있다.
- 문제에서 정렬 구현을 요구하지 않는다면, 표준 라이브러리를 불러와서 쓰도록 하자.
- 각 알고리즘 별 유리한 상황
  - 삽입 정렬: 리스트가 거의 정렬되어 있는 경우
  - 퀵 정렬: 일반적인 경우. 오히려 정렬된 경우가 worst
  - 계수 정렬
    - 데이터 크기 범위가 제한되어 있으며
    - 정수 형태로 표현할 수 있을 때

### 네 가지 정렬 알고리즘 간단 비교

|     알고리즘     |   선택 정렬   |  삽입 정렬  |     퀵 정렬     |   계수 정렬   |
| :--------------: | :-----------: | :---------: | :-------------: | :-----------: |
| 평균 시간 복잡도 |   $O(N^2)$    |  $O(N^2)$   |   $O(NlogN)$    |   $O(N+K)$    |
|     $\Omega$     | $\Omega(N^2)$ | $\Omega(N)$ | $\Omega(NlogN)$ | $\Omega(N+K)$ |
|   공간 복잡도    |    $O(N)$     |   $O(N)$    |     $O(N)$      |   $O(N+K)$    |

- 이때, N: 데이터의 개수, K: max(data)

## 들어가며

- 정렬
  - 데이터를 특정한 기준에 따라 순서대로 나열한 것
- 문제 상황에 따라 적절한 정렬 알고리즘이 공식처럼 사용된다
  - 데이터가 적을 때
  - 데이터가 많지만 데이터범위가 한정되어 있을 때
  - 데이터가 이미 어느정도 정렬되어 있을 때
- 정렬별 특징
  1. 아이디어가 매우 간단하다 (selection sort)
  2. 데이터가 거의 정렬되어 있을 때 매우 빠르다 (insertion sort)
  3. 대부분의 경우에 가장 적합하며, 충분히 빠르다 (quick sort, merge sort)
  4. 데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르다. (counting sort)

## 선택 정렬

- 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다
- 일단 기존의 매소드는 최소한으로 사용하고 기본에 충실해서 구현하도록 해보자

- 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교
  - 선택 정렬 성능 측정 : 35.8414..
  - 기본 정렬 라이브러리 : 0.0013.. (array.sort())

## 삽입 정렬

- 맨 앞 원소부터 선택해서 정렬
- 정렬된 원소들 | 정렬 전 원소들,
- 정렬 전 원소의 첫 원소가 정렬 대상 원소
- 정렬된 원소들의 마지막 원소부터 비교해서 위치 교환하는 식으로 바른 자리 찾아가기

- 코드 구현 후 배울점
  - 바로 직전 칸과 비교하기에, i를 업데이트할 필요가 없고 j, j-1로 하면 됨 :)
  - reverse range인 경우 range(start, end-1, -1)을 하면 된다. (검색해서 찾음. 눈에 익혀두자)
- 삽입 정렬의 시간복잡도
  - $O(N^2)$
- 삽입 정렬이 유리한 상황
  - 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다
  - 이미 정렬되어 있는 경우 == Best case :: O(N)

## 퀵 정렬

- "기준 데이터를 설정"(pivot) 하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
- 병합 정렬(머지 소트)과 더불어 프로그래밍 언어 정렬 라이브러리의 근간이 되는 알고리즘(C++, python, ..., quick+merge 하이브리드)
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터로 설정한다.

- 퀵 정렬 매커니즘

  - pivot을 정한다.(보통은 원소의 첫 elmt이다)
  - 피봇을 제외한 나머지의 array 왼쪽 끝에서부터 시작해서 pivot보다 큰 값이 나오면 선택,
  - array의 오른쪽 끝에서 부터 pivot보다 작은 값이 나오면 선택
  - 선택된 두 숫자를 교환한다
  - 이를 반복하다가, left와 right의 위치가 엇갈리는 경우, pivot과 작은 데이터의 위치를 서로 변경한다
  - 이제 p 왼쪽에 p보다 작은 숫자, 오른쪽에 p보다 큰 숫자로 분할되었다.
  - 왼쪽, 오른쪽에 대해 각각 퀵 정렬을 수행한다
  - 정렬이 재귀적으로 순환, 정렬의 범위가 점점 좁아짐

- 퀵 정렬이 빠른 이유

  - 0 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수 O(NlogN)을 기대할 수 있다
  - 너비 N \* 높이 logN (높이가 절반씩 줄어듬)

- 퀵 정렬의 시간 복잡도

  - 평균 O(NlogN)
  - WorstCase: O(N\*\*2) : 이미 오름차순/내림차순으로 정렬되어 있는 경우
    - 실제 다양한 프로그래밍언어에서 퀵정렬을 기반으로 정렬 라이브러리가 작성되어있다면
    - 최악의 경우에도 O(NlogN)을 보장하도록 알고리즘을 짠다
      - 내 생각: pivot을 첫 요소가 아니라 랜덤 선택? 음..
        - merge sort와의 하이브리드랬으니 머지 소트 듣고난 후에 고민 더 해보자
      - 실제: 머지소트 공부 후, 고민 후 알아보기

- 정석 퀵정렬 & 파이썬의 간단 퀵정렬(list comprehension) 비교
  - 정석 퀵정렬은 피봇에 대해 분할 이전까지 O(N)의 수행 시간이 걸린다,
  - 간단 버전에서 list comprehension은 2번 일어나므로 O(2N)이다.

## 계수 정렬 (카운팅 정렬)

- 특정 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
  - 데이터 크기 범위가 제한되어
  - 정수 형태로 표현할 수 있을 때
- 데이터 개수가 N, 데이터 중 최대값이 K일 때 최악의 경우에도
  수행 시간 O(N+K)를 보장한다

- 계수 정렬의 매커니즘

  - 1. 가장 작은 데이터부터 가장 큰 데이터 범위가 모두 담길 수 있도록 리스트를 생성한다
  - 1-1. 위의 array에서 min: 0, max: 9
  - 각각의 데이터가 몇 번 나왔는지 counting 후
    생성한 리스트에 기록
  - 결과를 확인할 때는 리스트의 첫 번째 데이터부터 하나씩
    그 값 만큼 반복하여 인덱스를 출력한다

- 계수 정렬의 복잡도 분석
  - 시간, 공간 복잡도 모두 O(N+K)
  - 때에 따라 심각한 비효율성을 초래할 수 있다.
    - e.g. 데이터가 0 혹은 999,999 단 2개만 있는 경우
  - 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적
    - 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기에 계수 정렬이 효과적