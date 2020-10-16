#!/usr/bin/env python
# coding: utf-8

# ## 6. ZigZag Conversion
# 
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# ```
# P   A   H   N
# A P L S I I G
# Y   I   R
# ```
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string s, int numRows);
#  
# 
# Example 1:
# ```
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# ```
# Example 2:
# ```
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# ```
# Example 3:
# ```
# Input: s = "A", numRows = 1
# Output: "A"
# ``` 
# 
# Constraints:
# 
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

# In[ ]:


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #iteration 1 "P" row[0] 
        #iteration 2 "A" row[1] +1
        #iteration 3 "Y" row[2] +1
        #iteration 4 "P" row[1] -1
        #iteration 5 "A" row[0] -1
        #iteration 6 "L" row[1] +1
        #iteration 7 "I" row[2] +1
        #iteration 8 "S" row[1] -1
        #iteration 9 "H" row[0] -1
        # ...
        
        # row == 0: step = 1
        # row == numRows - 1: step = -1
        # row += step
        if numRows == 1 or numRows >= len(s):
          return s
        
        zigzag = ['' for x in range(numRows)]
        
        row, step = 0, 1
        
        for crct in s:
          zigzag[row] += crct
          
          if row == 0:
            step = 1
          elif row == numRows - 1:
            step = -1
          
          row += step
        
        return ''.join(zigzag)

