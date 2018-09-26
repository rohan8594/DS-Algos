# Given a string,determine if it is comprised of all unique characters. For example, 
# the string 'abcde' has all unique characters and should return True. The string 'aabcde' 
# contains duplicate characters and should return false.

def uniqueChars(s):
    seen = set()

    for i in range(len(s)):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            return False

    return True

print(uniqueChars("abcdefg"))
print(uniqueChars("abcdefgg"))