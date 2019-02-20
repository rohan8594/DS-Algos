# CTCI Question 1.3


def URLify(s, trueLength):
    result = []

    for i in range(trueLength):
        if s[i] == ' ':
            result.append('%20')
        else:
            result.append(s[i])

    return ''.join(result)

#print(URLify('Mr John Smith    ', 13))
