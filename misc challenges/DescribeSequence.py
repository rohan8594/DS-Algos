def describeSequence(s):

    if len(s) < 1:
        return 1

    curDigit = s[0]
    curCount = 1
    result = ''

    for cur in s[1:]:
        if cur == curDigit:
            curCount += 1
        else:
            result += str(curCount) + curDigit
            curDigit = cur
            curCount = 1
    return result + str(curCount) + curDigit


print(describeSequence(''))
print(describeSequence('1211'))
print(describeSequence('1111'))
