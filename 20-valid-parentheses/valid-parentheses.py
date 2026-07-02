class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['{', '[', '(']:
                stack.append(c)
            if c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        return not stack