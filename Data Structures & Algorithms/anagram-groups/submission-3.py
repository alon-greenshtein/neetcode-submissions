from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        
        for x in strs:
            s["".join(sorted(x))].append(x)
       
        return list(s.values())