package arrayandstring;

/** 67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
*/

public class AddBinary {
    public static String addBinary(String a, String b) {
        String term1; 
        String term2;
        int term1_length;
        int term2_length;
        boolean temp = false;
        if (a.length() >= b.length()) {
            term1 = a; 
            term2 = b;
            term1_length = a.length();
            term2_length = b.length();
        }
        else {
            term1 = b; 
            term2 = a; 
            term1_length = b.length();
            term2_length = a.length();
        }
        int terms_length_delta = term1_length - term2_length;
        StringBuilder res = new StringBuilder();

        for (int i = term1_length-1; i >=0; i--) {
            boolean term1_char = (Character.getNumericValue(term1.charAt(i)) == 1);
            boolean term2_char;
            if (i - terms_length_delta >= 0 ) {
                term2_char = (Character.getNumericValue(term2.charAt(i-terms_length_delta)) == 1);
            }
            else { 
                term2_char = false; 
            }
            if (term1_char & term2_char & temp) {
                res.append(1);
                temp = true;    // 1
            }
            else if (term1_char & term2_char || term1_char & temp || term2_char & temp) {
                res.append(0);
                temp = true;    // 1      
            }
            else if (term1_char | term2_char | temp) {
                res.append(1);
                temp = false;                
            }
            else {
                res.append(0);
                temp = false; 
            }
        }
        if (temp == true) { 
            res.append(1);
        }

        return res.reverse().toString();
    }

    public static void main (String[] args) {
        //  String str1 = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";
        //  String str2 = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";
        String str1 = "1010";
        String str2 = "1011";

        // the answer
        System.out.println("Ans: ");
        System.out.println(addBinary(str1, str2));
    }

}