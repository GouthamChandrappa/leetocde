# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true 
# if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
from typing import List
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    # Add padding to simplify edge case handling
    flowerbed = [0] + flowerbed + [0]
    
    for i in range(1, len(flowerbed) - 1):
        # Check if the current plot and its neighbors are empty
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n  -= 1

            if n == 0: # If all flowers are planted, return True
                return True
    
    return n <= 0  # Return True if n <= 0, else False
if __name__ == "__main__":
# Example usage
    flowerbed1 = [1, 0, 0, 0, 1]
    n1 = 1
    print(canPlaceFlowers(flowerbed1, n1))  # Output: True

    flowerbed2 = [1, 0, 0, 0, 1]
    n2 = 2
    print(canPlaceFlowers(flowerbed2, n2))  # Output: False
