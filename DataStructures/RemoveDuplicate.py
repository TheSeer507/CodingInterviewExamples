#Given an Integer array nums sorted in non-decreasing order. remove the duplicates in-place such that each unique element appears only once
#Do not allocate extra memory
#In this problem, the key point to focus on is the input array being sorted.
#Best approach is to have 2 pointers, L and R and compare between them in each iteration


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l