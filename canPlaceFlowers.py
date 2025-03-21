"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for spot in range(len(flowerbed)):
            if flowerbed[spot] == 0: 
                left_empty = (spot == 0) or (flowerbed[spot - 1] == 0)  
                right_empty = (spot == len(flowerbed) - 1) or (flowerbed[spot + 1] == 0)  
                if left_empty and right_empty: 
                    flowerbed[spot] = 1
                    n -= 1
                
                if n == 0:  
                    return True
        
        return n <= 0  

        
        