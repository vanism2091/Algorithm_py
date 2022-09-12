from typing import *
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
You are given an array prices 
where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day 
to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 아래를 바탕으로 조금 다듬었는데(빠른 풀이+책풀이), 2392ms. 
        # 테스트 데이터가 바뀐듯.
        # 어쨌든, 계속 min, max 돌리는거보다는 빠르게 나옴 = 할당하지 않아서 그런가..
        min_price = sys.maxsize
        profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price
        return profit
        
        # 다른 더 빠른 풀이(969ms)
        minPrice = float('inf')
        # price보다는 profit이 맞는듯..
        maxPrice = 0
        
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxPrice:
                maxPrice = price - minPrice
        # 어차피 0보다 크지 않은 경우는 0 밖에 없음
        return maxPrice
        # return maxPrice if maxPrice > 0 else 0


        # sol_2-book 저점과 현재 값과의 차이 계산
        profit = 0
        min_price = sys.maxsize
        
        # 최소값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
        
        # sol_1-book brute-force
            # Timeout
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
        return max_price

        # mine
        b = s = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < b:
                max_profit = max(max_profit, s - b)
                b = s = prices[i]
            elif prices[i] > s:
                s = prices[i]
        return max(max_profit, s-b)
        
s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))