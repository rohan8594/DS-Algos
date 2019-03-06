# CTCI Question 1.9


def isSubstring(s1, s2):
    if s2 in s1:
        return True
    return False


def isStringRotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return isSubstring(s1 + s1, s2)


# testing
if isStringRotation("waterbottle", "erbottlewat"):
    print("Test 1 Passed")

if not isStringRotation("waterbottle", "nope"):
    print("Test 2 Passed")

if not isStringRotation("waterbottlewater", "waterbottle"):
    print("Test 3 Passed")
