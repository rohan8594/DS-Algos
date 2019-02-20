# CTCI Question 1.4


def palindromePerm(S):
    charCounts = {}
    S = S.lower().replace(' ', '')
    oddCount = 0

    for cur in S:
        if cur not in charCounts:
            charCounts[cur] = 1
        else:
            charCounts[cur] += 1

    for curKey in charCounts.keys():
        if charCounts[curKey] % 2 != 0:
            oddCount += 1

    if oddCount > 1:
        return False

    return True


print(palindromePerm('Tact Coa'))
print(palindromePerm('code'))
print(palindromePerm('aab'))
print(palindromePerm('carerac'))
