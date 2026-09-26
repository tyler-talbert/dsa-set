class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        goal = total // k
        
        # Not divisible with remainder of 0
        if total % k:
            return False

        nums.sort(reverse = True)
        used = [False] * len(nums)

        def dfs(i, subset_sum, remaining):
            if remaining == 0:
                return True
            if subset_sum == goal:
                return dfs(0, 0, remaining - 1)

            for j in range(i, len(nums)):
                if used[j] or subset_sum + nums[j] > goal:
                    continue
                used[j] = True
                if dfs(j, subset_sum + nums[j], remaining):
                    return True
                used[j] = False

                if subset_sum == 0:
                    return False

            return False
        
        return dfs(0, 0, k)

            

        