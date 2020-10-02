#!/usr/bin/env python
# coding: utf-8

# ## 122. Best Time to Buy and Sell Stock II
# 
# Say you have an array prices for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# In[ ]:


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_prof = 0
        
        for i, item in enumerate(prices):
          if i>0:
              if prices[i] > prices[i-1]:
                 max_prof += prices[i] - prices[i-1]
        return max_prof

