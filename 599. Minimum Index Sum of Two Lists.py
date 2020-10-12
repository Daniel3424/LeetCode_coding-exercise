#!/usr/bin/env python
# coding: utf-8

# ## 599. Minimum Index Sum of Two Lists
# 
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
# 
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
# 
#  
# 
# Example 1:
# ```
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# ```
# Example 2:
# ```
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
# ```
# Example 3:
# ```
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
# ```
# Example 4:
# ```
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
# ```
# Example 5:
# ```
# Input: list1 = ["KFC"], list2 = ["KFC"]
# Output: ["KFC"]
# ``` 
# 
# Constraints:
# 
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the stings of list1 are unique.
# All the stings of list2 are unique.

# In[ ]:


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        rest_list = dict()
        com = True
        
        for i in range(len(list1)):
          rest_name = list1[i]
          rest_list[rest_name] = i
          
        min_index = 20000
        min_name = []
        
        for j in range(len(list2)):
          rest_name = list2[j]
          if rest_name in rest_list:
            s = rest_list[rest_name]
            if min_index > s + j:
              min_name = [rest_name]
              min_index = s + j
            elif min_index == s + j:
              min_name.append(rest_name)
              
        return min_name

