#!/usr/bin/env python
# coding: utf-8

# ## 1417. Reformat The String
# 
# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
# 
# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
# 
# Return the reformatted string or return an empty string if it is impossible to reformat the string.
# 
#  
# 
# Example 1:
# ```
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
# ```
# Example 2:
# ```
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digits.
# ```
# Example 3:
# ```
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by characters.
# ```
# Example 4:
# ```
# Input: s = "covid2019"
# Output: "c2o0v1i9d"
# ```
# Example 5:
# ```
# Input: s = "ab123"
# Output: "1a2b3"
# ```
# 
# Constraints:
# 
# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.

# In[ ]:


class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        sList = list(s)
        char = []
        nums = []
        
        for s in sList:
          if s.isalpha() == True:
            char.append(s)
          if s.isnumeric() == True:
            nums.append(s)
            
        if abs(len(char) - len(nums)) >= 2:
          return ""
        elif len(char) > len(nums):
          while nums:
            ans.append(char.pop())
            ans.append(nums.pop())
          ans.append(char.pop())
          
        elif len(char) <= len(nums):
          while char:
            ans.append(nums.pop())
            ans.append(char.pop())
            
          if len(nums) != 0:
            ans.append(nums.pop())
            
        return "".join(ans)

