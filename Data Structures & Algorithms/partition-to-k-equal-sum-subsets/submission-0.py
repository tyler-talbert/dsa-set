class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False

        nums.sort(reverse = True)
        target = total // k
        used = [False] * len(nums)

        def dfs(i, k, subset_sum):
            if k == 0:
                return True
            if subset_sum == target:
                return dfs(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or subset_sum + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j + 1, k, subset_sum + nums[j]):
                    return True

                used[j] = False
                if subset_sum == 0:
                    return False
            return False
                
                

        
        return dfs(0, k, 0)

       