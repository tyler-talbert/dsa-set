class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        best = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                length = r - l + 1
                best = min(length, best)

                total -= nums[l]
                l += 1

        return best if best != float('inf') else 0


        
        