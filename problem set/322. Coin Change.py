class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i][j] -> 给定第i种物品拼出总重为j的物品所需硬币个数
        # dp[1][1] = min(dp[0][1], dp[1][0]+1)
        # dp[3][1] = min(dp[2][1], dp[])
        dp = [[float("inf") for _ in range(amount+1)] for _ in range(len(coins)+1)]
        dp[0][0] = 0
        for i in range(1, len(coins)+1):
            dp[i][0] = 0
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j>=coins[i-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][amount] if dp[-1][amount]!=float("inf") else -1