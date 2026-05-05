class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c.lower() for c in s if c.isalnum())
        
        if len(clean) <= 1:
            return True

        start = 0
        end = len(clean) - 1

        while clean[start] == clean[end]:
            start += 1
            end -= 1
            if start > end:
                return True

        return False
