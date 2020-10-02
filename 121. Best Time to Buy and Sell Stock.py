#!/usr/bin/env python
# coding: utf-8

# ## 121. Best Time to Buy and Sell Stock
# 
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# 
# Note that you cannot sell a stock before you buy one.

# In[ ]:


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
          return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, len(prices)):
          if prices[i] < min_price:
            min_price = prices[i]
          max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

