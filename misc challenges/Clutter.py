import collections


def generate_phases(phrases):
    phraseMap = collections.defaultdict(list)
    res = []

    for phrase in phrases:
        phraseMap[phrase.split()[0]].append(phrase)

    for phrase in phrases:
        phrase = phrase.split()

        if phrase[-1] in phraseMap:
            for cur in phraseMap[phrase[-1]]:
                res.append(' '.join(phrase[:-1]) + " " + cur)
    return res


input = [
    'mission statement',
    'a quick bite to eat',
    'a chip off the old block',
    'chocolate bar',
    'mission impossible',
    'a man on a mission',
    'block party',
    'eat my words',
    'bar of soap'
]

print(generate_phases(input))
