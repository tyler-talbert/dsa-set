class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False

        target = total // k
        nums.sort(reverse=True)
        consumed = [False] * len(nums)

        def combination_search(i, cur_sum, partitions_remaining):
            if not partitions_remaining:
                return True

            for j in range(i, len(nums)):
                candidate_sum = cur_sum + nums[j]
                if (consumed[j]) or (candidate_sum > target):
                    continue
                elif candidate_sum < target:
                    consumed[j] = True
                    if combination_search(j + 1, candidate_sum, partitions_remaining):
                        return True
                else:
                    consumed[j] = True
                    if combination_search(0, 0, partitions_remaining - 1):
                        return True

                consumed[j] = False

            return False

        return combination_search(0, 0, k)
