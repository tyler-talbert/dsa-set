class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        
        for key, v in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (v, key)) # freq, value
            else:
                if heap and heap[0][0] < v:
                    heapq.heappushpop(heap, (v, key)) 

        return [num for _, num in heap]
        



        