class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right =0, len(nums)-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
        

soln = Solution()
print(soln.findPeakElement([1, 2, 7, 4, 5]))

            
                





