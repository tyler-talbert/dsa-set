class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = prevprev = 1

        for i in range(2, n + 1):
            cur = prev + prevprev
            prevprev = prev
            prev = cur
        
        return cur

        