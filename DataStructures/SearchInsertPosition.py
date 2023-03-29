#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
# the index where it would be if it were inserted in order.
#Runtime complexity must be O(log n)

#Input: nums = [1,3,5,6], target = 5
#Output: 2

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #We are going to use binary search for maximum efficiency
        #we are targeting the idx of the nums array
        #l = 0 amd r is one less the lenght of array
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid -1
        return l