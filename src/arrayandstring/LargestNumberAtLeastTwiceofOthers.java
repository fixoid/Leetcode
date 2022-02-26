package arrayandstring;
/** 747. Largest Number At Least Twice of Others
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
 */

public class LargestNumberAtLeastTwiceofOthers {  
    public static int dominantIndex(int[] nums) {
        int largest = 0; 
        int prelargest = 0; 
        int largest_index = -1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > prelargest){
                if (nums[i] > largest) {
                    prelargest = largest;
                    largest = nums[i];
                    largest_index = i;
                }
                else { prelargest = nums[i]; }
            }
        }
        if (largest >= prelargest*2) { return largest_index; }
        else { return -1; }
    }

    public static void main (String[] args) {
        int[] nums = {1,7,3,6,5,6};
        // int[] nums = { -1,-1,-1,1,1,1 };
        System.out.println( dominantIndex(nums) );
    }
}