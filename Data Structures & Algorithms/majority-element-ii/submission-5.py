class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) == 3:
                for k in list(count):
                    count[k] -= 1
                    if not count[k]:
                        del count[k]

        return [k for k in count if nums.count(k) > len(nums) // 3]

        