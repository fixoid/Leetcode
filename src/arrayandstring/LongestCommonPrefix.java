package arrayandstring;
// 14. Longest Common Prefix
// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".
// Example 1:
// Input: strs = ["flower","flow","flight"]  # Output: "fl"
// Example 2:
// Input: strs = ["dog","racecar","car"]     # Output: ""
// Constraints:
// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lower-case English letters.

class Solution {
    public String longestCommonPrefix(String[] strs) {
        // check for empty list
        if ((strs == null) || (strs.length == 0)) {
            return "";
        }
        // getting last item of list as template
        String template = strs[0];
        // check for one item list (empty after poping item)
        if (strs.length == 0) {
            return template;
        }
        
        Integer pref_length = template.length();
        //  walking across the list for comparing items with template
        for (String str: strs) {
            // check for item length, and cuttint prefix length if needed
            if (str.length() < pref_length) {
                pref_length = str.length();
                template = template.substring(0, pref_length);
            }
            //  if item and template is not equal, we need to cut template and complare with item again
            // System.out.println(!str.substring(0,pref_length).equals(template));
            if (str.substring(0,pref_length).equals(template) == false) {
                System.out.println("qwe");
                while (pref_length > 0) {
                    pref_length -= 1;
                    
                    System.out.println(str.substring(0,pref_length) +" " + template.substring(0,pref_length));
                    //  if cutted item is equal with template, go to next item
                    if (str.substring(0,pref_length).equals(template.substring(0,pref_length))) {
                        template = template.substring(0,pref_length);
                        break;
                    }
                }
                System.out.println(pref_length);
                if (pref_length == 0) {
                    return "";
                }
                
            }
        }

        return template;
    }
}

public class LongestCommonPrefix {
    public static void main (String[] args) {
        String somelist[] = new String[] {"flower","flow","flight"};
        // String somelist[] = new String[] {"dog","racecar","car"};
        // String somelist[] = new String[] {""};
        // String somelist[] = new String[] {"ab","a"};
        // String somelist[] = new String[] {"aaa","aa","aaa"};
        Solution lcp = new Solution();
        System.out.println(lcp.longestCommonPrefix(somelist) );
    }

}
