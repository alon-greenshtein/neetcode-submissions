class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d ={
            ")": "(",
            "}": "{",
            "]": "["
        }
        for ch in s:
            if ch not in d:
                stack.append(ch)
            else:
                if not stack or d[ch] != stack[-1]:
                    return False
                stack.pop()
        
        return not stack


        