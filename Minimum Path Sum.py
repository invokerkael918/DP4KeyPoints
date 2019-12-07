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
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(2)]
        dp[0][0] = grid[0][0]
        for i in range(row):
            for j in range(col):
                if (i == 0 and j == 0):
                    continue
                if i == 0:
                    dp[0][j] = dp[0][j - 1] + grid[0][j]
                    continue
                if j == 0:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + grid[i][j]
                    continue
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[i % 2][j - 1]) + grid[i][j]
        return dp[(row - 1) % 2][col - 1]
