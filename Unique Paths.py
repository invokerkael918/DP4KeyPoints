class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        # n is col
        # m is row
        dp = [[0 for j in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m - 1][n - 1]


class Solution2:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        # n is col
        # m is row
        dp = [[0 for j in range(n)] for _ in range(m)]
        for row in dp:
            row[0] = 1
        dp[0] = [1] * n

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    S = Solution2().uniquePaths(3,3)

