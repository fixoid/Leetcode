package arrayandstring;

import java.util.HashMap;
import java.util.Map;

/** 28. Implement strStr()
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:
Input: haystack = "", needle = ""
Output: 0
*/

class ImplementStrStrBMHA {
    // Boyer–Moore–Horspool algorithm
    public static int strStr(String haystack, String needle) {
        if (needle == "" || needle == null || needle.isEmpty()) { return 0; }
        if (haystack == "" || haystack == null || haystack.isEmpty()) { return -1; }
        //represents strings as arrays and calculate strings length
        String[] haystack_arr = haystack.split(""); 
        String[] needle_arr = needle.split("");
        int haystack_len = haystack_arr.length;
        int needle_len = needle_arr.length;

        // create Pattern table dictionary for chars in needle (char : position of char from the end of needle)
        Map<String,Integer> pattern_table = new HashMap<String,Integer>();
        // and fill pattern table win
        for (int i=0; i <= needle_len-2 ; i++) {
            pattern_table.put(needle_arr[i], needle_len-1-i);
        }

        int pointer = needle_len-1; // current pointer for compare chars
        Integer skip = 0;      // how much chars in haystack we can skip
        System.out.println(pattern_table);
        while (pointer <= haystack_len-1) {
            //check if needle in start of string
            // comparing needle to haystack from right to left
            // if not moves pointer on _skip_ positions
            int j;
            for (j = 0; j <= needle_len-1; j++) {
                if (haystack_arr[pointer-j].equals(needle_arr[needle_len-1-j]) != true) {
                    // System.out.println(pointer + " -- " + j + " -- " + (pointer-j) + " -- " + haystack_arr[pointer-j] + " -- " + skip);
                    j = needle_len;
                }
                
            }
            // substring finded in the string
            if (j == needle_len) {
                return pointer-j+1;
            }
            // move pointer if substring did't find
            skip = pattern_table.get(haystack_arr[pointer]);
            if (skip == null) {  skip = needle_len;  }
            pointer+=skip;
            skip=0;
        }

        return -1;
    }

    public static void main (String[] args) {
        String str1 = "abaabbbbaaabbbaaa";
        String str2 = "bbbb";

        // the answer
        System.out.println("Ans: ");
        System.out.println(strStr(str1, str2));
    }

}