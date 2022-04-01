package arrayandstring;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

// 189. Rotate Array
// Given an array, rotate the array to the right by k steps, where k is non-negative.
// Example 1: Input: nums = [1,2,3,4,5,6,7], k = 3 Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]
// Example 2: Input: nums = [-1,-100,3,99], k = 2 Output: [3,99,-1,-100]
// Explanation: 
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]

// Constraints:
// 1 <= nums.length <= 105
// -231 <= nums[i] <= 231 - 1
// 0 <= k <= 105

// Follow up:
// Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
// Could you do it in-place with O(1) extra space?

public class RotateArray {
    // with two pointers
    public static void rotate(int[] nums, int k) {
        int nums_len = nums.length;
        k = k % nums_len;
        reverse(nums, 0, nums_len-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, nums_len-1);       
    }

    public static void reverse(int[] array, int left, int rigth) {
        while (left < rigth) {
            int temp;
            temp = array[left];
            array[left] = array[rigth];
            array[rigth] = temp;
            left++;
            rigth--;
        }

    }

    // makes copy of array and replays items from copy with move on k
    public static void rotate0(int[] nums, int k) {
        int nums_len = nums.length;
        k = k % nums_len;
        int nums_copy[] = new int[nums_len];
        System.arraycopy(nums, 0, nums_copy, 0, nums_len);
        for (int i = 0; i < k; i++) {
            nums[k-1-i] = nums_copy[nums_len - 1 - i];
        }
        for (int i = k; i < nums_len; i++) {
            nums[i] = nums_copy[i-k];
        }
    }

    //very slow, not accepted (time limit exeeded)
    public static void rotate1(int[] nums, int k) {
        int nums_len = nums.length;
        k = k % nums_len;
        List<Integer> result = Arrays.stream(nums).boxed().collect(Collectors.toList());
        for (int i = 0; i < k; i++) {
            result.add(0,result.remove(nums_len-1));
            
        }
        System.out.println(result);
        for(int i = 0; i < nums_len; i++) {
            nums[i] = result.get(i);
        }
    }
    
    public static void main (String[] args) {
        int nums[] = new int[] {1,2,3,4,5,6,7};
        int k = 3;
        RotateArray.rotate(nums, k);
        for (int num: nums) {
            System.out.print(num +" ");
        }
        System.out.println("");
    }
}
