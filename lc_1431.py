# return a boolean array speifying if the kid in the list has the highest number of candies.
from typing import List
class solution:
    def kidswithcandies(self, candies: List[int], extracandies: int) -> List[bool]:
        max_candies = max(candies)

        result =[]
        
        for  candies in candies:
            if candies+extracandies >= max_candies:
                result.append("true")
            else:
                result.append("false")
        return result


if __name__ == "__main__":

    candies = [2,3,4,5,8]
    extracandies = 5
    print(solution().kidswithcandies(candies, extracandies))

            
            