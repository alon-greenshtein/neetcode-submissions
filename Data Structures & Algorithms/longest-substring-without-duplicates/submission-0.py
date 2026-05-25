class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        seen = set()
        l = r = 0
        lon = 0

        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            lon = max(lon, r - l + 1)
            r += 1


        return lon
        