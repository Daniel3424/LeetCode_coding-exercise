#!/usr/bin/env python
# coding: utf-8

# ## 409. Longest Palindrome
# 
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# In[ ]:


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
          return 0
        
        vals = list(Counter(s).values())
        
        evens = 0
        highestOdd = 0
        
        for v in vals:
          if v%2 == 0:
            evens += v
          else:
            highestOdd = max(highestOdd, v)
            
        return evens+highestOdd

