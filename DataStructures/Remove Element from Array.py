#Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_,_]
#Explanation: Your function should return k = 2, with the first two elements of nums being 2.

#Approach use a pointer, k to shift the vallue to the right as long as it is not equal to vallue.

class Solution:
    def removeElement(self, nums: List[int], val:int) -> int:
        #Initialize out pointer
        k = 0
        #Loop through the lenght of nums array
        for i in range(len(nums)):
        #if the number in the current position is not equal to val we replace our pointer with the current position of nums array
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        #We return our pointer which holds the number of element in the nums array
        return k

#Anoter Approach, more efficient
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


#One Liner Python3 Implementation
class Solution3:
    def removeElement3(self, nums: List[int], val:int)-> int:
        while val in nums:nums.remove(val)