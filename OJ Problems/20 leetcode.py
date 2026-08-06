class Solution:
    def isValid(self, s: str) -> bool:
        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
            return False
        else:
            stack = []
            matches = {')': '(', ']': '[', '}': '{'}
            for char in s:
                if char in "({[":
                    stack.append(char)
                else:
                    if stack == [] or stack[-1] != matches[char]:
                        return False
                    stack.pop()
            return stack == []
        