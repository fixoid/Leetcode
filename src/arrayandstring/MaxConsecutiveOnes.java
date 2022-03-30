package arrayandstring;

// 485. Max Consecutive Ones
// Given a binary array nums, return the maximum number of consecutive 1's in the array.
// Example 1: Input: nums = [1,1,0,1,1,1] Output: 3
// Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
// Example 2: Input: nums = [1,0,1,1,0,1] Output: 2
// Constraints:
// 1 <= nums.length <= 105
// nums[i] is either 0 or 1.

class FindMaxConsecutiveOnes {
    public static int findMaxConsecutiveOnes(int[] nums) {
        int j = 0;
        int maxj = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                j ++;
            }
            else {
                if (maxj < j) { maxj = j; }
                j = 0;
            }
        }
        if (maxj < j) { maxj = j; }
        return maxj;
    }

    public static void main (String[] args) {
        int nums[] = new int[] {1,1,0,1,1,1};
        System.out.println(findMaxConsecutiveOnes(nums));
    }
}