# Given an input string, reverse the string word by word.

# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Example 3:

# Input: "a good   example"
# Output: "example good a"

# Note:

# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.


class Solution:
    def reverseWords(self, s: str) -> str:
        strArr = []
        curWord, res = "", ""

        # strArr = s.split(" ")
        for char in s:
            if char == " ":
                strArr.append(curWord)
                curWord = ""
                continue
            curWord += char
        strArr.append(curWord)

        for i in range(len(strArr) - 1, -1, -1):
            if strArr[i] == "":
                continue
            res += strArr[i] + " "

        return res[:-1]
