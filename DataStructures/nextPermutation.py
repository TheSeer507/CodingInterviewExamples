'''
The function takes an array of integers nums as input and modifies it in place to find the next permutation.
If there is no next permutation, the function reverses the array to give the lowest possible permutation.
'''

def nextPermutation(nums):
    i = len(nums) - 2
    # Find the first decreasing element from the right
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    # If there is no such element, the entire sequence is decreasing
    if i < 0:
        nums.reverse()
        return

    #Find the next greater element to the right of nums[i]
    j=len(nums)-1
    while j > i and nums[j] <= nums[i]:
        j -= 1
    
    #swap nums[i] and nums[j]
    nums[i], nums[j] = nums[j], nums[i]

    #reverse the elements to the right of i
    nums[i+1:] = reversed(nums[i+1:])
