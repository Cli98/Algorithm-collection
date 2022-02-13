class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums) + target
        if total%2>0:
            return 0
        target = abs(total//2)
        dp = [[0 for _ in range(target+1)] for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(target+1):
                if j>=nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]