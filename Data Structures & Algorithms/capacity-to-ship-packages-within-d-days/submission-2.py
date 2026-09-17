class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        best = r

        while l <= r:
            elapsed = 1
            cur_sum = 0
            m = (l + r) // 2
            
            for w in weights:
                if cur_sum + w > m:
                    cur_sum = w
                    elapsed += 1
                else:
                    cur_sum += w
            
            if elapsed <= days:
                best = m
                r = m - 1
            else:
                l = m + 1
            
        
        return best
                

                








        