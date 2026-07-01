#("home","about","career") : 2
# "home","cart","maps" : 1

# bob : ["home","about","career", "home","about","career"]
# alice : "home","cart","maps","home"
# charlie : "home","about","career"

from itertools import combinations
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        a = []
        p = defaultdict(list)
        v = defaultdict(int)

        for i in range(len(username)):
            a.append((timestamp[i],username[i],website[i]))
        a.sort()

        for i in range(len(a)):
            p[a[i][1]].append(a[i][2])

        for key in p:
            d = set(combinations(p[key], 3))
            for comb in d:
                v[comb] += 1

        hi = 0
        for x in v:
            hi = max(hi, v[x])
        
        res = []
        for x in v:
            if v[x] == hi:
                res.append(x)
        
        res.sort()

        return list(res[0])


        



