<<<<<<< HEAD
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

#Another Approach O(1) in space
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:

            for i in reversed(range(1, len(nums))):
                if nums[i] == nums[i-1]:
                    nums.pop(i)
            return len(nums)

#Another approach O(1) - One Liner
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            nums[:] = (n for i, n in enumerate(nums) if i == 0 or nums[i-1] != n)

#One Final Approach
class Solution:
    def removeDuplicates(self, nums: List[int], k=1) -> int:
        nums[:] = sorted(list(set(nums)))
<<<<<<< HEAD

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
=======
=======
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
>>>>>>> 1f12b88269c68e4e1b02aa59849a43f9ea5c59a0
        return l

