class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        target = (len(nums) // 3) + 1

        freq = Counter(nums)
        res = []

        for k, v in freq.items():
            if v >= target:
                res.append(k)

        return res


        