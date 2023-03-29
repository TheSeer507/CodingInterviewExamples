#Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
#Input: nums = [1,2,3,1]
#Output: true


#Easiest approach is with a hashset to store the values of the array
#most efficient and fastest.
#We then compare elements in the hash

class Solution:
    def constainsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False