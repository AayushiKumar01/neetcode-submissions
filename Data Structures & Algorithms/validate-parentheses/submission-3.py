class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if (len(stack) and (stack[-1] == '(' and s[i] == ')' or stack[-1] == '[' and s[i] == ']' or stack[-1] == '{' and s[i] == '}')):
                stack.pop()
            else:
                stack.append(s[i])
        
        if len(stack):
            return False
        return True

        