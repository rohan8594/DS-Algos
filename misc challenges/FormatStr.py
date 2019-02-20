# Design a function which corrects software keys.

# Function input is a string S and an integer K. The string is
# a mix of upper and lowercase alphanumeric characters
# partitioned with hyphens (possibly misplaced). The function
# should return the string S partitioned to have exactly K
# characters in each partition, except for possibly the first
# one (which may have as few as one character), and for the string to be all uppercase.

# So given input S = '2Kr7-a1-3j' and K = 4,
# the function should return '2KR7-A13J'.

# Given input S = 'r', K = 1,
# the function should return 'R'.

# HOWEVER, given input S = '2Kr7-a1-3j' and K = 3,
# the function should return `2K-R7A-13J`.

# You can assume that K is a positive integer >= 1.

# NOTE: Question is similar to license key formatting question from leetcode


def formatStr(S, K):
    result = []
    newStrArr = []
    counter = K

    for cur in S:
        if cur == '-':
            continue
        newStrArr.append(cur)

    if len(S) <= K:
        return ''.join(newStrArr).upper()

    for i in range(len(S)):
        if newStrArr:
            if counter == 0:
                counter = K
                result.append('-')
                continue
            result.append(newStrArr.pop())
            counter -= 1

        else:
            break

    return ''.join(result[::-1]).upper()
