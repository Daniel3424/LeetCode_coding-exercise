#!/usr/bin/env python
# coding: utf-8

# ## 1496. Path Crossing
# 
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# 
# Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.
# 
#  
# 
# Example 1:
# ```
# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.
# ```
# Example 2:
# ```
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
# ``` 
# 
# Constraints:
# 
# 1 <= path.length <= 10^4
# path will only consist of characters in {'N', 'S', 'E', 'W}

# In[ ]:


class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        visit = {}
        x,y = 0,0
        visit[(x,y)] = 1
        for i in path:
            if i == 'N':
                y -= 1
            elif i == 'S':
                y += 1
            elif i == 'E':
                x += 1
            else:
              x -= 1
            if (x,y) in visit:
              return True
            visit[(x,y)] = 1
        return False

