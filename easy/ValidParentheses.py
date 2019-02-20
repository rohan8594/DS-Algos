# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()[]{}"
# Output: true

# Example 3:

# Input: "([)]"
# Output: false


def validParentheses(s):
    stack = []
    paren_dict = {")": "(", "]": "[", "}": "{"}

    for curr in s:
        if curr in paren_dict.values():
            stack.append(curr)

        if stack == []:
            return False

        if curr in paren_dict.keys():
            if stack.pop() != paren_dict[curr]:
                return False

    return stack == []


print(validParentheses("{()[]}"))
print(validParentheses("([)]"))
