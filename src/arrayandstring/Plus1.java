package arrayandstring;

/** Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
 */

public class Plus1 {  
    // Fast
    public static int[] plusOne(int[] digits) {
        //if (digits == null || digits.length == 0) { return 0; }
        for(int i = digits.length-1; i>=0; i--) {
            if (digits[i] < 9) {
                digits[i] += 1;
                return digits;
            }
            else {
                digits[i] = 0;
            }
        }
        // if all digits was 9, need to resize ans array and set 1st digit to 1
        int[] ans = new int[digits.length + 1];
        ans[0] = 1; 
        return ans;
    }
    // Slow (able to modify for plus and integer)
    public static int[] plusOneAlt(int[] digits) {
        int[] pre_ans = new int[digits.length+1];
        System.arraycopy(digits, 0, pre_ans, 1, digits.length);
        pre_ans[digits.length] += 1;
        for (int i = pre_ans.length-1; i>0; i--) {
            pre_ans[i-1] += pre_ans[i]/10;
            pre_ans[i] %= 10;
        }
        if (pre_ans[0] == 0) {
            return java.util.Arrays.copyOfRange(pre_ans, 1, pre_ans.length);
        }
        else {
            return pre_ans;
        }
    }


    public static void main (String[] args) {
        int[] nums = {9,9,9,9,9};
        // int[] nums = { 1,3,3,4,5,9 };
        System.out.println( java.util.Arrays.toString(plusOne(nums)) );
    }
}