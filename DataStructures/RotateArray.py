#Given an array, rotate the array to the right by k steps, where k is non-negative.
#Example
#nums = [1,2,3,4,5,6,7], k = 3
# Result should be [5,6,7,1,2,3,4]

#Best approach is a tripple rotation using 3 while loops

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k = k % len(nums)
        l, r = 0, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1