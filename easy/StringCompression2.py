# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.

# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Example 2:
# Input:
# ["a"]

# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]

# Example 3:
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        curr_char = chars[0]
        curr_count = 1
        i = 0
        len_of_chars = len(chars)

        for curr in chars[1:]:
            if curr == curr_char:
                curr_count += 1
            else:
                if curr_count == 1:
                    chars.insert(i, curr_char)
                    i += 1
                else:
                    if len(str(curr_count)) > 1:
                        chars.insert(i, curr_char)
                        i += 1
                        for x in str(curr_count):
                            chars.insert(i, x)
                            i += 1
                    else:
                        chars.insert(i, curr_char)
                        i += 1
                        chars.insert(i, str(curr_count))
                        i += 1
                curr_char = curr
                curr_count = 1

        if curr_count == 1:
            chars.insert(i, curr_char)
            i += 1
        else:
            if len(str(curr_count)) > 1:
                chars.insert(i, curr_char)
                i += 1
                for x in str(curr_count):
                    chars.insert(i, x)
                    i += 1
            else:
                chars.insert(i, curr_char)
                i += 1
                chars.insert(i, str(curr_count))
                i += 1

        for i in range(len_of_chars):
            chars.pop()

        return len(chars)
