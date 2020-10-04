#!/usr/bin/env python
# coding: utf-8

# ## 171. Excel Sheet Column Number
# 
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# 
# ```
# For example:
# 
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# ```

# In[ ]:


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        maps = {}
        for i in range(26):
          maps[let[i]] = i + 1
        
        col = 0 
        for l in s:
            col = 26*col + maps[l]
          
        return col

