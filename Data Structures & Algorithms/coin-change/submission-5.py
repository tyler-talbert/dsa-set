class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [float('inf')] * (amount + 1)
        amounts[0] = 0

        coins.sort()

        for i in range(amount + 1):
            if amounts[i] != float('inf'):
                for coin in coins:
                    if coin + i > amount:
                        break
                    amounts[coin + i] = min(amounts[coin + i], amounts[i] + 1)
        
        return -1 if amounts[amount] == float('inf') else amounts[amount]
                
            

            

        