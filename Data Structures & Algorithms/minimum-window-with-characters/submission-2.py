from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ls = len(s)
        lt = len(t)
        if lt > ls:
            return ""
        l = 0
        r = 0
        cs = Counter()
        ct = Counter(t)
      
        sw = "a" * (ls + 1)
        w = sw
        while r <= ls:
            while ct <= cs:
                w = s[l:r]
                cs[s[l]] -= 1
                if cs[s[l]] == 0:
                    del cs[s[l]]
                l += 1
            if len(sw) > len(w):
                sw = w
            if r == ls:
                break
            cs[s[r]] += 1    
            r += 1
            
        
        if sw == ("a" * (ls + 1)):
            return ""
        return sw
            

            
           

        