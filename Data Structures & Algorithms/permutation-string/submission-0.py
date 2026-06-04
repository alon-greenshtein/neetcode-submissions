from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n:
            return False
        l = 0
        c = Counter(s1)

        while l + n - 1 < len(s2):
            c1 = c.copy()
            for j in range(l,l + n):
                if s2[j] not in c1:
                    break
                c1[s2[j]] -= 1
                if c1[s2[j]] == 0:
                    del c1[s2[j]]
            if not c1:
                return True
            l += 1

        return False

        