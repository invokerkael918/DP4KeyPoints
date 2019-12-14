class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        s = [0] * (n + 1)
        # s : sum from right to left, s[i] means if 1 coin left, how much value we could get
        # values : [1,2,2]
        #       s: [2,4,5] if only 1 coin left, we can only get 2 (the last value),
        #                  if 2 coins left, the max value we could get is 4
        #       dp[i] : 还剩下i时，先手可以获得的最大价值，如果此价值大于总价值的一半，则先手可以赢
        #       dp[i]最大，则dp[i-1] dp[i-2]要最小，dp[i-1] dp[i-2]为对手可取的两个值，我们要取这两个的最小
        #       stat transfer formula : dp[i] = sum(i) - min(dp[i-1],dp[i-2])
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + values[n - i]
        dp[0] = 0
        dp[1] = values[n - 1]
        for i in range(2, n + 1):
            dp[i] = s[i] - min(dp[i - 1], dp[i - 2])
        return dp[n] > s[n] / 2
