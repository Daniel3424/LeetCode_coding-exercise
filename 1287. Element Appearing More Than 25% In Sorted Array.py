#!/usr/bin/env python
# coding: utf-8

# ## 1287. Element Appearing More Than 25% In Sorted Array
# 
# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.
# 
# Return that integer.
# 
# 
# Example 1:
# ```
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# ``` 
# 
# Constraints:
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5

# In[ ]:


class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        b = n * 0.25
        for i in range(n):
          if i == 0:
            prev = arr[i]
            cnt = 1
          elif prev == arr[i]:
            cnt += 1
          else:
            cnt = 1
            prev=arr[i]
          
          if cnt>b:
            return arr[i]

