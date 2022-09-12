# 7장 배열

## 문제
출처: [algorithm-interview 깃헙](https://github.com/onlybooks/algorithm-interview/blob/master/README.md)

| 번호 | 제목 | 난이도 | 장 | 풀이 코드 |
| --- | --- | ---- | - | --- |
| 7 | [두 수의 합](https://leetcode.com/problems/two-sum/) | ★ | 7장. 배열 | [07_1.py](07_1.py)|
| 8 | [빗물 트래핑](https://leetcode.com/problems/trapping-rain-water/) | ★★★ | 7장. 배열 | [08_42.py](08_42.py) |
| 9 | [세 수의 합](https://leetcode.com/problems/3sum/) | ★★ | 7장. 배열 | [09_15.py](09_15.py) |
| 10 | [배열 파티션 I](https://leetcode.com/problems/array-partition-i/) | ★ | 7장. 배열 | [10_561.py](10_561.py) |
| 11 | [자신을 제외한 배열의 곱](https://leetcode.com/problems/product-of-array-except-self/) | ★★ | 7장. 배열 | [11_238.py](11_238.py) |
| 12 | [주식을 사고팔기 가장 좋은 시점](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | ★ | 7장. 배열 | [12_121.py](12_121.py) |

## 간단 정리
### 투 포인터

### 최댓값과 최솟값
- 최댓값과 최솟값은 문제의 제약 상황에 따라 정의에 따라 잘 설정해야 한다.
- 최대값을 규정할 수 없는 경우 임의의 값을 사용하지 않는 편이 좋다.
- `sys.maxsize` 또는 `float('-inf')`를 사용하면 안전하다.

