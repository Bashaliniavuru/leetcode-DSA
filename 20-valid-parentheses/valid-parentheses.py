class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pair={"]":"[","}":"{",")":"("}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
                continue
            if not stack:
                return False
            if stack[-1]!=pair[ch]:
                return False
            else:
                stack.pop()
        if not stack:
            return True
        else:
            return False

        