class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack
        my_stack = []
        for c in s:
            if c in ('[', '(', '{'):
                my_stack.append(c)
            elif not my_stack:
                return False
            elif c == ']':
                if my_stack.pop() != '[':
                    return False
            elif c == ')':
                if my_stack.pop() != '(':
                    return False
            elif c == '}':
                if my_stack.pop() != '{':
                    return False
        return len(my_stack) == 0