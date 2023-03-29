<<<<<<< HEAD
class Solution{
    public int pivotIndex(int[] nums){
        int totalSum = 0;
        int leftSum = 0;
        for(int ele: nums)
            totalSum += ele;
        for (i = 0; i < nums.length; leftSum += nums[i++])
            if (leftSum * 2 == totalSum - nums[i])
                return i;

        return -1;
    }
=======
class Solution{
    public int pivotIndex(int[] nums){
        int totalSum = 0;
        int leftSum = 0;
        for(int ele: nums)
            totalSum += ele;
        for (i = 0; i < nums.length; leftSum += nums[i++])
            if (leftSum * 2 == totalSum - nums[i])
                return i;

        return -1;
    }
>>>>>>> f950a5d03e56eb5bdcef8829000dc223c6260333
}