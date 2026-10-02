class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        wildcard = []

        for i in range(len(s)):
            if s[i] == "(":
                left.append(i)
            elif s[i] == ")":
                if left:
                    left.pop()
                elif wildcard:
                    wildcard.pop()
                else:
                    return False
            elif s[i] == "*":
                wildcard.append(i)
            
        while left and wildcard:
            if left.pop() > wildcard.pop():
                return False # open bracket appears after star, so cannot be closed

        return not left