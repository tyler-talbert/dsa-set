class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(cur_amount):
            if cur_amount == amount:
                return 0
            if cur_amount > amount:
                return float('inf')
            if cur_amount in cache:
                return cache[cur_amount]

            count = float('inf')

            for coin in coins:
                count = min(count, 1 + dfs(cur_amount + coin))

            cache[cur_amount] = count
            return cache[cur_amount]

        result = dfs(0)
        return -1 if result == float('inf') else result
        