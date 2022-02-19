package arrayandstring;
/** Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
*/

public class FindPivotIndex {    
    // Faster - with presum
    public static int pivotIndex(int[] nums) {
        int[] presum = new int[nums.length]; 
        presum[0] = nums[0];
        int sum_left = 0; 
        int sum_rigth; 
        for (int i = 1; i < nums.length; i++) {
            presum[i] = presum[i-1] + nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            if(i > 0) { sum_left = presum[i-1]; }
            sum_rigth = presum[(presum.length-1)] - presum[i]; 
            // System.out.println(nums.length + " " + i + " " + presum[i] );
            if (sum_left == sum_rigth) { return i; }
        }
        return -1;
    }
    // Slower
    public static int pivotIndex2(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int sum_left = 0; 
            int sum_rigth = 0; 
            if (i > 0) { 
                for (int j = 0; j < i; j++) {
                    sum_left += nums[j];
                }
            }
            if (i < (nums.length-1)) { 
                for (int j = i+1; j < (nums.length); j++) {
                    sum_rigth += nums[j];
                }
            }
            if (sum_left == sum_rigth) { return i; }
        }
        return -1;
    }

    public static void main (String[] args){
        int[] nums = {1,7,3,6,5,6};
        // int[] nums = { -1,-1,-1,1,1,1 };
        System.out.println( pivotIndex(nums) );
    }
}