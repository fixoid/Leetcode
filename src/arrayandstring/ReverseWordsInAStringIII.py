# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1: Input: s = "Let's take LeetCode contest" Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2: Input: s = "God Ding" Output: "doG gniD"
# Constraints:
# 1 <= s.length <= 5 * 10**4
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

class Solution:
    # fast with splitting string on array of words
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        for i in range(len(arr)):
            arr[i] = "".join(arr[i][::-1])
        
        return " ".join(arr)
    
    # very slow with splitting string on array of chars and two pointers :)     
    def reverseWords1(self, s: str) -> str:
        arr = [char for char in s]
        arr_len = len(arr)
        slow = 0
        fast = 0
        while (fast < arr_len):
            if arr[fast] == " ":
                self.reverse(arr, slow, fast-1)
                slow = fast+1
            elif fast == arr_len-1:
                self.reverse(arr, slow, fast)
            fast += 1

        return "".join(arr)

    def reverse(self, arr, left, rigth):
        while(left < rigth):
            arr[left], arr[rigth] = arr[rigth], arr[left]
            left += 1
            rigth -= 1


if __name__ == "__main__":
    somestr = "Let's take LeetCode contest"
    sol = Solution()
    print(sol.reverseWords1(somestr))