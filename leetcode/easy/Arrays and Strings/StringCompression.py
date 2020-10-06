# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
# For this problem, you can falsely "compress" strings of single or double letters.
# For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes
# more space.

# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.


def compress(s):
    result = ""

    curr_item = s[0]
    curr_count = 1
    for curr in s[1:]:
        if curr != curr_item:
            result += curr_item + str(curr_count)
            curr_item = curr
            curr_count = 1
        else:
            curr_count += 1
    result += curr_item + str(curr_count)

    return result
