class MySolution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False

        if n == 2 or n == 1:
            return True

        dp = [0] * (n)
        dp[0] = dp[1] = True

        for i in range(2, n):

            if dp[i - 1] and dp[i - 2]:
                dp[i] = False
                continue
            dp[i] = True

        return dp[-1]


class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        # write your code here

        dp = [False] * 3
        dp[1] = dp[2] = True

        for i in range(n):
            dp[i % 3] = not dp[(i - 1) % 3] or not dp[(i - 2) % 3]

        return dp[n % 3]
