# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1: Input: s = "abcabcbb" Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2: Input: s = "bbbbb" Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3: Input: s = "pwwkew" Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Constraints: 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    # hashtable and sliding window solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        rigth = 0
        hash = {}
        longest_sub = 0
        while rigth < len(s):
            if s[rigth] not in hash:
                hash[s[rigth]] = True
                rigth +=1
                if len(hash) > longest_sub: 
                    longest_sub = len(hash)
            else:
                hash.pop(s[left])
                left += 1
        return longest_sub

if __name__ == "__main__":
    s = "abcabdcbabd"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
            