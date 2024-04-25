class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char == ')' and (not stack or stack.pop() != '('):
                return False
            elif char == '}' and (not stack or stack.pop() != '{'):
                return False
            elif char == ']' and (not stack or stack.pop() != '['):
                return False

        return not stack



