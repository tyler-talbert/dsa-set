class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        requirement = len(nums) // 3
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1

            if len(count) < 3:
                continue

            copy = count.copy()
            for k in copy.keys():
                count[k] -= 1
                if not count[k]:
                    count.pop(k, None)

        for k in count.keys():
            count[k] = 0

            for num in nums:
                if num == k:
                    count[k] += 1
        
        for k, v in count.items():
            if v > requirement:
                res.append(k)

        return res

        