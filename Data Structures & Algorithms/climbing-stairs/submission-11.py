class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(position):
            if position > n:
                return 0
            if position == n:
                return 1
            if position in cache:
                return cache[position]

            res = dfs(position + 1) + dfs(position + 2)

            cache[position] = res
            return cache[position]
        
        res = dfs(0)
        return res

        