# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]  # Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]     # Output: ""
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

from typing import List

class Solution:

    def __init__(self) -> None:
        pass

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # check for empty list
        if strs == None or len(strs) == 0 or (len(strs) == 1 and len(strs[0]) == 0) :
            return ''
        # getting last item of list as template
        template = strs.pop()
        # check for one item list (empty after poping item)
        if len(strs) == 0:
            return template
        
        pref_length = len(template)

        # walking across the list for comparing items with template
        for str in strs:
            # check for item length, and cuttint prefix length if needed
            if len(str) < pref_length:
                pref_length = len(str)
                template = template[0:pref_length]
            # if item and template is not equal, we need to cut template and complare with item again
            if str[0:pref_length] != template:
                while (pref_length > 0):
                    pref_length -= 1
                    # if cutted item is equal with template, go to next item
                    if str[0:pref_length] == template[0:pref_length]:
                        template = template[0:pref_length]
                        break
            else:
                pass

        return template

if __name__ == "__main__":
    somelist = list(["flower","flow","flight"])
    somelist = list(["dog","racecar","car"])
    # somelist = list([''])
    # somelist = list(["ab", "a"])
    # somelist = list(["aaa","aa","aaa"])
    sol = Solution()
    print(sol.longestCommonPrefix(somelist))