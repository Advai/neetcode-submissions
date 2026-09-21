import heapq # heapq is always min-heap btw
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iter through, get count of each element
        # iter through keys 
        freq = Counter(nums)                 # value -> count, O(n)
        min_heap = []
        for value, count in freq.items():
            heapq.heappush(min_heap, (count, value))   # order by count
            if len(min_heap) > k:
                heapq.heappop(min_heap)                # evict current smallest

        return [value for count, value in min_heap]
        