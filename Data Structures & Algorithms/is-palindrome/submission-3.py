class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        start = 0
        end = len(s) - 1

        while start < len(s) and not s[start].isalnum():
            start += 1

        while not s[end].isalnum() and end >= 0:
            end -= 1

        if start > end:
            return True

        while s[start].lower() == s[end].lower():
            start += 1
            end -= 1

            while start < len(s) and not s[start].isalnum():
                start += 1

            while end >= 0 and not s[end].isalnum():
                end -= 1

            if start > end:
                return True

        return False
