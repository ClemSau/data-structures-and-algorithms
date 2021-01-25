# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        matches = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in matches:
                stack.append(c)
            else:
                if not stack or c != matches[stack.pop()]:
                    return False
        return not stack
