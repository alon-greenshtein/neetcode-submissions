import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        res = []

        for i,x in c.items():
            heapq.heappush(h, (-x,i))
        for j in range(k):
            res.append(heapq.heappop(h)[1])
        
        return res


