class Solution(object):
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in s:
            if bracket in '([{':
                stack.append(bracket)

            else:
                if not stack:
                    return False

                top = stack.pop()

                if top != pairs[bracket]:
                    return False

        return len(stack) == 0

