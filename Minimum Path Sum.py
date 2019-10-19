class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        """
        :type n: int row
        :type m: int col
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for i in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]

        for j in range(m):
            for i in range(n):
                if i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                    continue
                if i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[n - 1][m - 1]


if __name__ == '__main__':
    a = [[1, 3], [1, 5]]
    b = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    S = Solution().minPathSum(b)
    print(S)
