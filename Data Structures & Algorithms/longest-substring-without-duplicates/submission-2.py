class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        l = 0
        lon = 0

        for r in range(n):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)

            seen[s[r]] = r
            lon = max(lon, r - l + 1)
            
        return lon
        