package arrayandstring;
/** Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
 */

public class Plus1 {  
    public static int[] plusOne(int[] digits) {

        return digits;   
    }


    public static void main (String[] args) {
        int[] nums = {1,7,3,6,5,6};
        // int[] nums = { 1,3,3,4,5,9 };
        System.out.println( plusOne(nums) );
    }
}