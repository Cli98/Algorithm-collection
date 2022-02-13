class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        def Remove_dup(strs):
            # item -> k
            result = {}
            for s in strs:
                if s not in result:
                    result[s] = 1
                else:
                    result[s] += 1
            return result

        def Count(s):
            zero = one = 0
            for char in s:
                if char == '0':
                    zero += 1
                else:
                    one += 1
            return zero, one

        strs_count = Remove_dup(strs)
        strs = list(strs_count.keys())
        dp = [[[float("-inf") for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for j in range(m + 1):
            for k in range(n + 1):
                dp[0][j][k] = 0
        hashmap = {}
        for s in strs:
            hashmap[s] = Count(s)

        for i in range(1, len(strs_count) + 1):
            zero, one = hashmap[strs[i - 1]]
            cur_str_count = strs_count[strs[i - 1]]
            for j in range(m + 1):
                for k in range(n + 1):
                    l = 1
                    while l < cur_str_count + 1:
                        if j >= l * zero and k >= l * one:
                            dp[i][j][k] = max([dp[i][j][k], dp[i - 1][j][k], dp[i - 1][j - l * zero][k - l * one] + l])
                        else:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
                        l += 1
        return dp[-1][-1][-1] if dp[-1][-1][-1] != float("-inf") else 0