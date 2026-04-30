from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        for x in strs:
            s["".join(sorted(x))].append(x)
        res = []
        for i in s.values():
            res.append(i)
        return res